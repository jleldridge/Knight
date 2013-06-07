import pygame, math
from pygame.locals import *

ALPHA_COLOR = (255, 0, 255)

class Enemy(pygame.sprite.Sprite):
    
    STUCK_X = "stuck_x"
    STUCK_Y = "stuck_y"
    
    def __init__(self, image, rect, attack_power, attack_force, solid=False, 
    solid_rect=None, attack_rect=None, hittable_rect=None):
        pygame.sprite.Sprite.__init__(self)
        
        # create a list to keep track of observed information
        self.observation = {'stuck_x': False, 'stuck_y': False}
        # create a list to keep track of all of the rects
        self.rects = []
        
        self.image = image
        
        self.rect = rect
        self.rects.append(self.rect)
        
        self.attack_power = attack_power
        self.attack_force = attack_force
        self.solid = solid
        
        if (not solid_rect) and solid:
            self.solid_rect = rect
        else:
            self.solid_rect = solid_rect    
        if self.solid_rect:
            self.rects.append(self.solid_rect)
        
        self.attack_rect = attack_rect
        if self.attack_rect:
            self.rects.append(attack_rect)
        
        self.hittable_rect = hittable_rect
        if self.hittable_rect:
            self.rects.append(hittable_rect)
        
        self.max_x_speed = 0
        self.max_y_speed = 0
        self.visited_rects = []
    
    
    def update(self, player, map):
        # prepare to execute this enemy's next move
        pass
    
    def greedy_chase(self, goal, map, clear_counter):
        # clear visited_rects every few updates
        if clear_counter == 0:
            self.visited_rects = []
        
        # goal is the point to approach and is of form (x, y)
        # generate the next possible moves
        moves = []
        moves.append((self.max_x_speed, 0))
        moves.append((0-self.max_x_speed, 0))
        moves.append((0, self.max_y_speed))
        moves.append((0, 0-self.max_y_speed))
        moves.append((self.max_x_speed, self.max_y_speed))
        moves.append((0-self.max_x_speed, 0-self.max_y_speed))
        
        # eliminate the moves that will collide with other objects/enemies
        if self.solid:
            for m in list(moves):
                # generate the rect representing this move
                r = self.solid_rect.move(m[0], m[1])
                
                for e in map.enemies:
                    if e.solid and e != self and r.colliderect(e.solid_rect):
                        try: moves.remove(m)
                        except: pass
                        self.visited_rects.append(r)
                for o in map.static_objects:
                    if o.solid and r.colliderect(o.solid_rect):
                        try: moves.remove(m)
                        except: pass
                        self.visited_rects.append(r)
                        
        
        # now find the move left in the list that gets closest to the goal
        best_distance = None
        best_move = None
        for m in moves:
            r = self.solid_rect.move(m[0], m[1])
            distance = math.sqrt((r.centerx-goal[0])**2 + (r.centery-goal[1])**2)
        
            if (((not best_move) or (distance < best_distance)) and 
                (not r in self.visited_rects)):
                best_distance = distance
                best_move = m
            
            self.visited_rects.append(r)
        
        # return the best move in the form (x_speed, y_speed)
        return best_move
        
        
    def move_x(self, distance):
        for rect in self.rects:
            rect.left += distance
    
    def move_y(self, distance):
        for rect in self.rects:
            rect.top += distance
            
    def observe(self, info, status):
        # receive info from the environment
        self.observation[info] = status

# Enemy definitions

class Slime(Enemy):
    
    def __init__(self, x, y):
        # slime will temporarily be a green square
        image = pygame.image.load("src/Slime.png").convert()
        image.set_colorkey(ALPHA_COLOR)
        rect = image.get_rect()
        rect.centerx = x
        rect.centery = y
        attack_power = 1
        attack_force = 8
        attack_rect = rect.inflate(-5, -5)
        hittable_rect = rect.copy()
        solid_rect = attack_rect.copy()
        Enemy.__init__(self, image, rect, attack_power, attack_force, True, 
            solid_rect, attack_rect, hittable_rect)
        
        self.aggro_distance = 400
        self.x_speed = 0
        self.y_speed = 0
        self.max_x_speed = 1
        self.max_y_speed = 1
        
        self.chase_counter = 100
    
    def update(self, player, map):
        # prepare to execute this enemy's next move
        distance_to_player = math.sqrt((self.attack_rect.centerx-player.rect.centerx)**2
            + (self.attack_rect.centery-player.rect.centery)**2)
        
        move = None
        
        if distance_to_player <= self.aggro_distance:
            move = self.greedy_chase((player.rect.centerx, player.rect.centery), 
                map, self.chase_counter)
        
        if self.chase_counter > 0:
            self.chase_counter -= 1
        elif self.chase_counter <= 0:
            self.chase_counter = 100
        
        if move:
            self.x_speed = move[0]
            self.y_speed = move[1]
        else:
            self.x_speed = 0
            self.y_speed = 0
    
    
    
    
    