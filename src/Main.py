import pygame, sys, math
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAP_TILE_SIZE = 32

# set up the game
pygame.init()
main_clock = pygame.time.Clock()

# create the game window
main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("Knight")

import Player, Image_Utils, Tilesets, Maps

# create the submap_image here instead of in draw() for speed
submap_image = pygame.Surface((1024, 1024)).convert()

def handle_events(events, player):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # this method could be dolled up a bit to account for 2 opposite keys
        # being pressed
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                # keys_down['left'] = True
                # keys_down['right'] = False
                player.x_speed = 0 - player.max_x_speed
            if event.key == K_RIGHT or event.key == ord('d'):
                # keys_down['right'] = True
                # keys_down['left'] = False
                player.x_speed = player.max_x_speed
            if event.key == K_UP or event.key == ord('w'):
                # keys_down['up'] = True
                # keys_down['down'] = False
                player.y_speed = 0 - player.max_y_speed
            if event.key == K_DOWN or event.key == ord('s'):
                # keys_down['down'] = True
                # keys_down['up'] = False
                player.y_speed = player.max_y_speed
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                # keys_down['left'] = False
                player.x_speed = 0
            if event.key == K_RIGHT or event.key == ord('d'):
                # keys_down['right'] = False
                player.x_speed = 0
            if event.key == K_UP or event.key == ord('w'):
                # keys_down['up'] = False
                player.y_speed = 0
            if event.key == K_DOWN or event.key == ord('s'):
                # keys_down['down'] = False
                player.y_speed = 0

                
def update_game(player, map):
    # move the player based on their speed and check for collisions
    
    # move in x direction, checking for collisions
    player.rect.left += player.x_speed
    for enemy in map.enemies:
        if player.rect.colliderect(enemy.attack_rect):
            player.health -= enemy.attack_power
            if player.x_speed < 0:
                player.rect.left += enemy.attack_force
            else:
                player.rect.left -= enemy.attack_force
        if enemy.solid and player.rect.colliderect(enemy.solid_rect):
            if player.x_speed < 0:
                player.rect.left = enemy.solid_rect.right
            else:
                player.rect.right = enemy.solid_rect.left
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
            if player.y_speed < 0:
                player.rect.top += enemy.attack_force
            else:
                player.rect.top -= enemy.attack_force
        if enemy.solid and player.rect.colliderect(enemy.solid_rect):
            if player.y_speed < 0:
                player.rect.top = enemy.solid_rect.bottom
            else:
                player.rect.bottom = enemy.solid_rect.top
    for object in map.static_objects:
        if object.solid and player.rect.colliderect(object.solid_rect):
            if player.y_speed < 0:
                player.rect.top = object.solid_rect.bottom
            else:
                player.rect.bottom = object.solid_rect.top
    
    # move player based on the buttons down and check for collisions
    # REMEMBER: when you get to it, let player attack rects hit before probably anything else
    # NOTE: the current order of things causes the player to 'teleport' to the other side of static_objects when pushed by an enemy's attacks
    # if keys_down['left']:
        # player.rect.left -= player.x_speed
        # for enemy in map.enemies:
            # if player.rect.colliderect(enemy.attack_rect):
                # player.health -= enemy.attack_power
                # player.rect.left += enemy.attack_force
            # if enemy.solid and player.rect.colliderect(enemy.solid_rect):
                # player.rect.left = enemy.solid_rect.right
        # for object in map.static_objects:
            # if object.solid and player.rect.colliderect(object.solid_rect):
                # player.rect.left = object.solid_rect.right
    # if keys_down['right']:
        # player.rect.left += player.x_speed
        # for enemy in map.enemies:
            # if player.rect.colliderect(enemy.attack_rect):
                # player.health -= enemy.attack_power
                # player.rect.left -= enemy.attack_force
            # if enemy.solid and player.rect.colliderect(enemy.solid_rect):
                # player.rect.right = enemy.solid_rect.left
        # for object in map.static_objects:
            # if object.solid and player.rect.colliderect(object.solid_rect):
                # player.rect.right = object.solid_rect.left
    # if keys_down['up']:
        # player.rect.top -= player.y_speed
        # for enemy in map.enemies:
            # if player.rect.colliderect(enemy.attack_rect):
                # player.health -= enemy.attack_power
                # player.rect.top += enemy.attack_force
            # if enemy.solid and player.rect.colliderect(enemy.solid_rect):
                # player.rect.top = enemy.solid_rect.bottom
        # for object in map.static_objects:
            # if object.solid and player.rect.colliderect(object.solid_rect):
                # player.rect.top = object.solid_rect.bottom
    # if keys_down['down']:
        # player.rect.top += player.y_speed
        # for enemy in map.enemies:
            # if player.rect.colliderect(enemy.attack_rect):
                # player.health -= enemy.attack_power
                # player.rect.top -= enemy.attack_force
            # if enemy.solid and player.rect.colliderect(enemy.solid_rect):
                # player.rect.bottom = enemy.solid_rect.top  
        # for object in map.static_objects:
            # if object.solid and player.rect.colliderect(object.solid_rect):
                # player.rect.bottom = object.solid_rect.top   

def draw(main_window, player, map):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    main_window.fill(BLACK)
    
    # find which tile of the map the player is on
    player_map_x = int(player.rect.centerx/MAP_TILE_SIZE)
    player_map_y = int(player.rect.centery/MAP_TILE_SIZE)
    player_x_offset = player.rect.centerx-(player_map_x*32)
    player_y_offset = player.rect.centery-(player_map_y*32)
    
    # create a 2-d list to hold the tiles of the map that we will draw
    submap = []
    for i in range(32):
        temp_row = []
        for j in range(32):
            map_row = player_map_y-16+i
            map_col = player_map_x-16+j
            if ((map_row>=0) and (map_col>=0) and (map_row<len(map.layout)) and 
                (map_col<len(map.layout[0]))):
                temp_row.append(map.layout[map_row][map_col])
            else:
                temp_row.append(-1)
        submap.append(temp_row)
            
    # draw the necessary part of the map
    submap_image.fill(BLACK)
    for i in range(32):
        for j in range(32):
            if submap[i][j] < 0:
                submap_image.blit(map.blank_tile, (j*32, i*32))
            else:
                submap_image.blit(map.tileset[submap[i][j]], (j*32, i*32))
    
    # if a static game object falls within the submap and is a background object,
    # draw it before the player
    # REMEMBER: eventually want to change exactly what x, y coordinates to draw
    # from based on the object's collision rectangle
    for object in map.static_objects:
        object_tile_x = int(object.rect.centerx/MAP_TILE_SIZE)
        object_tile_y = int(object.rect.centery/MAP_TILE_SIZE)
        
        if ((object_tile_x > player_map_x-16) and 
            (object_tile_y > player_map_y-16) and
            (object_tile_x <= player_map_x+16) and 
            (object_tile_y <= player_map_y+16) and
            (object.background)):
            # draw the object based on its offset from the player
            object_x_offset = object.rect.left-player.rect.centerx+player_x_offset
            object_y_offset = object.rect.top-player.rect.centery+player_y_offset
            submap_image.blit(object.image, 
                (512+object_x_offset, 512+object_y_offset))
    
    # draw the player to the submap_image
    submap_image.blit(player.image, 
        (512-int(player.rect.width/2)+player_x_offset, 
        512-int(player.rect.height/2)+player_y_offset))
    
    # draw the enemies onto the submap_image
    for enemy in map.enemies:
        enemy_tile_x = int(enemy.rect.centerx/MAP_TILE_SIZE)
        enemy_tile_y = int(enemy.rect.centery/MAP_TILE_SIZE)
        if ((enemy_tile_x > player_map_x-16) and 
            (enemy_tile_y > player_map_y-16) and
            (enemy_tile_x <= player_map_x+16) and 
            (enemy_tile_y <= player_map_y+16)):
            enemy_x_offset = enemy.rect.left-player.rect.centerx+player_x_offset
            enemy_y_offset = enemy.rect.top-player.rect.centery+player_y_offset
            submap_image.blit(enemy.image, 
                (512+enemy_x_offset, 512+enemy_y_offset))

    # if a static game object falls within the submap, draw it
    # REMEMBER: eventually want to change exactly what x, y coordinates to draw
    # from based on the object's collision rectangle
    for object in map.static_objects:
        object_tile_x = int(object.rect.centerx/MAP_TILE_SIZE)
        object_tile_y = int(object.rect.centery/MAP_TILE_SIZE)
        
        if ((object_tile_x > player_map_x-16) and 
            (object_tile_y > player_map_y-16) and
            (object_tile_x <= player_map_x+16) and 
            (object_tile_y <= player_map_y+16) and
            (not object.background)):
            # draw the object based on its offset from the player
            object_x_offset = object.rect.left-player.rect.centerx+player_x_offset
            object_y_offset = object.rect.top-player.rect.centery+player_y_offset
            submap_image.blit(object.image, 
                (512+object_x_offset, 512+object_y_offset))
    
    screen_centerx = int(WINDOW_WIDTH/2)
    screen_centery = int(WINDOW_HEIGHT/2)
    
    # draw the map_subimage to the screen
    main_window.blit(submap_image, (screen_centerx-512-player_x_offset,
        screen_centery-512-player_y_offset))
    
    # draw the player at the center of the screen
    # main_window.blit(player.image, (screen_centerx-int(player.rect.width/2), 
        # screen_centery-int(player.rect.height/2)))
    
    # debug player x and y coordinates
    # font = pygame.font.Font(None, 30)
    # xstring = "x: " + str(player.rect.centerx)
    # ystring = "y: " + str(player.rect.centery)
    # pos_text = font.render(xstring + "   " + ystring, False, WHITE)
    # main_window.blit(pos_text, (10, 10))
    # offset_string = ("x offset: " + str(player_x_offset) + "   y offset: " + 
        # str(player_y_offset))
    # offset_text = font.render(offset_string, False, WHITE)
    # main_window.blit(offset_text, (10, 30))

def main():
    keys_down = {'up': False, 'down': False, 'left': False, 'right': False}
    
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
        draw(main_window, player, map)
        
        pygame.display.flip()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        