import pygame, sys
import Player, Image_Utils
from pygame.locals import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
MAP_TILE_SIZE = 32

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

def draw(main_window, player, game_objects, map, tileset):
    BLACK = (0, 0, 0)
    main_window.fill(BLACK)
    
    # find the player's map position
    player_map_x = player.rect.center[0]/MAP_TILE_SIZE
    player_map_y = player.rect.center[1]/MAP_TILE_SIZE
    
    # draw the necessary part of the map
    map_subimage = pygame.Surface((1024, 1024))
    for i in range(1024/32):
        for j in range(1024/32):
            map_subimage.blit(tileset[map[player_map_y-(player_map_y-i)]
                [player_map_x-(player_map_x-j)],
                (32*i, 32*j, MAP_TILE_SIZE, MAP_TILE_SIZE))
    
    # draw the map to the screen
    main_window.blit(map_subimage, )

def main():
    game_objects = []
    keys_down = {'up': False, 'down': False, 'left': False, 'right': False}
    
    player = Player.Player()
    player.rect.x = 800/2
    player.rect.y = 600/2
    game_objects.append(player)
    
    # set up the game
    pygame.init()
    main_clock = pygame.time.Clock()
    
    # create the game window
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Knight")
    
    # temporary map
    map = []
    for i in range(200):
        row = []
        for j in range(200):
            row.append(30)
        map.append(row)
    
    # temporary tileset
    tileset = Image_Utils.load_tileset("Castle.png", 512, 512, 32, 32)
            
    # main loop
    while True:
        # handle events
        handle_events(pygame.event.get(), keys_down)
        
        # update the game
        update_game(player, game_objects, keys_down)
        # draw game objects
        draw(main_window, player, game_objects, map, tileset)
        
        pygame.display.update()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        