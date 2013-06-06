import pygame, sys, math
from pygame.locals import *

flags = DOUBLEBUF

X_RESOLUTION = 1280
Y_RESOLUTION = 800
MAP_TILE_SIZE = 32

# set up the game
pygame.init()
main_clock = pygame.time.Clock()

# create the game window
screen = pygame.display.set_mode((X_RESOLUTION, Y_RESOLUTION), flags, 32)
screen.set_alpha(None)
pygame.display.set_caption("Knight")

import Player, Image_Utils, Tilesets, Maps

keys_down = {'left': False, 'right': False, 'up': False, 'down': False}

def handle_events(events, player):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                keys_down['left'] = True
            if event.key == K_RIGHT or event.key == ord('d'):
                keys_down['right'] = True
            if event.key == K_UP or event.key == ord('w'):
                keys_down['up'] = True
            if event.key == K_DOWN or event.key == ord('s'):
                keys_down['down'] = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                keys_down['left'] = False
            if event.key == K_RIGHT or event.key == ord('d'):
                keys_down['right'] = False
            if event.key == K_UP or event.key == ord('w'):
                keys_down['up'] = False
            if event.key == K_DOWN or event.key == ord('s'):
                keys_down['down'] = False
        
    # set player speed based on keys down and status effects
    if (not player.knockback):
        # left and right
        if keys_down['left'] and not keys_down['right']:
            player.x_speed = 0 - player.max_x_speed
        elif keys_down['right'] and not keys_down['left']:
            player.x_speed = player.max_x_speed
        else:
            player.x_speed = 0
        
        # up and down
        if keys_down['up'] and not keys_down['down']:
            player.y_speed = 0-player.max_y_speed
        elif keys_down['down'] and not keys_down['up']:
            player.y_speed = player.max_y_speed
        else:
            player.y_speed = 0
                
def update_game(player, map):
    # move the player based on their speed and check for collisions
    # REMEMBER: when you get to it, let player attack rects hit before probably anything else
    # move in x direction, checking for collisions
    player.rect.left += player.x_speed
    for enemy in map.enemies:
        if player.rect.colliderect(enemy.attack_rect):
            player.health -= enemy.attack_power
            # hitting the enemy knocks the player back based on the attack force
            player.knockback = enemy.attack_force
            if player.x_speed < 0:
                player.x_speed = player.knockback_speed
                player.rect.left = enemy.attack_rect.right
            else:
                player.rect.right = enemy.solid_rect.left
                player.x_speed = 0 - player.knockback_speed
        if enemy.solid and player.rect.colliderect(enemy.solid_rect):
            if player.x_speed < 0:
                player.rect.left = enemy.solid_rect.right
            else:
                player.rect.right = enemy.solid_rect.left
    #only check solid object collisions if the player is moving
    if(player.x_speed):
        for object in map.static_objects:
            if object.solid and player.rect.colliderect(object.solid_rect):
                if player.x_speed < 0:
                    player.rect.left = object.solid_rect.right
                else:
                    player.rect.right = object.solid_rect.left

    # move in y direction, checking for collisions
    player.rect.top += player.y_speed
    for enemy in map.enemies:
        if player.rect.colliderect(enemy.attack_rect):
            player.health -= enemy.attack_power
            # hitting the enemy knocks the player back based on attack force
            player.knockback = enemy.attack_force
            if player.y_speed < 0:
                player.rect.top = enemy.solid_rect.bottom
                player.y_speed = player.knockback_speed
            else:
                player.rect.bottom = enemy.solid_rect.top
                player.y_speed = 0 - player.knockback_speed
        if enemy.solid and player.rect.colliderect(enemy.solid_rect):
            if player.y_speed < 0:
                player.rect.top = enemy.solid_rect.bottom
            else:
                player.rect.bottom = enemy.solid_rect.top
    #only check solid object collisions if the player is moving
    if(player.y_speed):
        for object in map.static_objects:
            if object.solid and player.rect.colliderect(object.solid_rect):
                if player.y_speed < 0:
                    player.rect.top = object.solid_rect.bottom
                else:
                    player.rect.bottom = object.solid_rect.top
    
    # reduce the knockback counter if it is still above 0
    if player.knockback:
        player.knockback -= 1
        if player.knockback == 0:
            player.x_speed = 0
            player.y_speed = 0

def draw(screen, player, map):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    screen.fill(BLACK)
    
    screen_left = int(player.rect.centerx - X_RESOLUTION/2)
    screen_top = int(player.rect.centery - Y_RESOLUTION/2)
    screen_rect = pygame.Rect(screen_left, screen_top, X_RESOLUTION, 
        Y_RESOLUTION)
    
    # draw the screen
    for row in map.layout:
        for tile in row:
            if tile.rect.colliderect(screen_rect):
                # draw the tile to screen
                screen.blit(tile.image, (tile.rect.left-screen_rect.left, 
                    tile.rect.top-screen_rect.top))
    
    # draw static objects that the player should be in front of
    for object in map.static_objects:
        if object.background:
            if object.rect.colliderect(screen_rect):
                screen.blit(object.image, (object.rect.left-screen_rect.left,
                    object.rect.top-screen_rect.top))
    
    # draw the player to the screen
    player_draw_x = int(X_RESOLUTION/2 - player.rect.width/2)
    player_draw_y = int(Y_RESOLUTION/2 - player.rect.height/2)
    screen.blit(player.image, (player_draw_x, player_draw_y))
    
    # draw static objects that the player should be behind
    for object in map.static_objects:
        if not object.background:
            if object.rect.colliderect(screen_rect):
                screen.blit(object.image, (object.rect.left-screen_rect.left,
                    object.rect.top-screen_rect.top))
    
    # draw the enemies
    for enemy in map.enemies:
        if enemy.rect.colliderect(screen_rect):
            screen.blit(enemy.image, (enemy.rect.left-screen_rect.left, 
                enemy.rect.top-screen_rect.top))


def main():
    player = Player.Player()
    player.rect.centerx = 0
    player.rect.centery = 0
    
    # temporary map
    map = Maps.Map01()
            
    # main loop
    while True:
        # handle events
        handle_events(pygame.event.get(), player)
        
        # update the game
        update_game(player, map)
        # draw game objects
        draw(screen, player, map)
        
        pygame.display.flip()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        