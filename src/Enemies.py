import pygame, math
from pygame.locals import *

ALPHA_COLOR = (255, 0, 255)

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, image, rect, attack_power, attack_force, solid=False, 
    solid_rect=None, attack_rect=None, hittable_rect=None):
        pygame.sprite.Sprite.__init__(self)
        
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
    
    def update(self):
        # execute this enemy's ai
        pass

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
        
        self.aggro_distance = 200
        self.x_speed = 0
        self.y_speed = 0
        self.max_x_speed = 1
        self.max_y_speed = 1
    
    
    def update(self, player):
        # find out how close the player is
        distance = math.sqrt((player.rect.centerx-self.rect.centerx)**2 + 
            (player.rect.centery-self.rect.centery)**2)
            
        x_distance = player.rect.centerx - self.rect.centerx
        y_distance = player.rect.centery - self.rect.centery
        
        # if the player is within aggro range, move towards the player
        if distance <= self.aggro_distance:
            if abs(x_distance) > abs(y_distance):
                self.y_speed = 0
                if x_distance < 0:
                    self.x_speed = 0 - self.max_x_speed
                else:
                    self.x_speed = self.max_x_speed
            elif abs(y_distance) > abs(x_distance):
                self.x_speed = 0
                if y_distance < 0:
                    self.y_speed = 0 - self.max_y_speed
                else:
                    self.y_speed = self.max_y_speed
            else:
                if x_distance < 0:
                    self.x_speed = 0 - self.max_x_speed
                else:
                    self.x_speed = self.max_x_speed
                if y_distance < 0:
                    self.y_speed = 0 - self.max_y_speed
                else:
                    self.y_speed = self.max_y_speed
        else:
            self.x_speed = 0
            self.y_speed = 0
    
    def move_x(self):
        for rect in self.rects:
            rect.left += self.x_speed
    
    
    def move_y(self):
        for rect in self.rects:
            rect.top += self.y_speed
    
    
    
    
    