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

def handle_events(events, keys_down):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                keys_down['left'] = True
                keys_down['right'] = False
            if event.key == K_RIGHT or event.key == ord('d'):
                keys_down['right'] = True
                keys_down['left'] = False
            if event.key == K_UP or event.key == ord('w'):
                keys_down['up'] = True
                keys_down['down'] = False
            if event.key == K_DOWN or event.key == ord('s'):
                keys_down['down'] = True
                keys_down['up'] = False
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                keys_down['left'] = False
            if event.key == K_RIGHT or event.key == ord('d'):
                keys_down['right'] = False
            if event.key == K_UP or event.key == ord('w'):
                keys_down['up'] = False
            if event.key == K_DOWN or event.key == ord('s'):
                keys_down['down'] = False

def update_game(player, game_objects, keys_down):
    # move player
    if keys_down['left']:
        player.rect.left -= player.x_speed
    if keys_down['right']:
        player.rect.left += player.x_speed
    if keys_down['up']:
        player.rect.top -= player.y_speed
    if keys_down['down']:
        player.rect.top += player.y_speed

def draw(main_window, player, game_objects, map):
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
    
    # draw the player to the submap_image
    submap_image.blit(player.image, 
        (512-int(player.width/2)+player_x_offset, 
        512-int(player.height/2)+player_y_offset))
    
    # if a static game object falls within the submap, draw it
    for object in map.static_objects:
        object_tile_x = int(object.x/MAP_TILE_SIZE)
        object_tile_y = int(object.y/MAP_TILE_SIZE)
        
        if ((object_tile_x > player_map_x-16) and (object_tile_y > player_map_y-16) and
            (object_tile_x <= player_map_x+16) and (object_tile_y <= player_map_y+16)):
            # draw the object based on its offset from the player
            object_x_offset = object.x-player.rect.centerx+player_x_offset
            object_y_offset = object.y-player.rect.centery+player_y_offset
            submap_image.blit(object.image, 
                (512+object_x_offset, 512+object_y_offset))
    
    screen_centerx = int(WINDOW_WIDTH/2)
    screen_centery = int(WINDOW_HEIGHT/2)
    
    # draw the map_subimage to the screen
    main_window.blit(submap_image, (screen_centerx-512-player_x_offset,
        screen_centery-512-player_y_offset))
    
    # draw the player at the center of the screen
    # main_window.blit(player.image, (screen_centerx-int(player.width/2), 
        # screen_centery-int(player.height/2)))
    
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
    game_objects = []
    keys_down = {'up': False, 'down': False, 'left': False, 'right': False}
    
    player = Player.Player()
    player.rect.centerx = 0
    player.rect.centery = 0
    game_objects.append(player)
    
    # temporary map
    map = Maps.map01
            
    # main loop
    while True:
        # handle events
        handle_events(pygame.event.get(), keys_down)
        
        # update the game
        update_game(player, game_objects, keys_down)
        # draw game objects
        draw(main_window, player, game_objects, map)
        
        pygame.display.update()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        