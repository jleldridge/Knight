import pygame, sys, math
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
    WHITE = (255, 255, 255)
    main_window.fill(BLACK)
    
    # find which tile of the map the player is on
    player_map_x = int(player.rect.centerx/MAP_TILE_SIZE)
    player_map_y = int(player.rect.centery/MAP_TILE_SIZE)
    
    # draw the whole map
    # map_image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    # start_tilex = math.floor(
        # ((len(map[0])*32)-player.rect.centerx-(WINDOW_WIDTH/2))/32
    # )
    # start_tiley = math.floor(
        # ((len(map)*32)-player.rect.centery-(WINDOW_HEIGHT/2))/32
    # )  
    # for i in range(start_tiley, start_tiley+math.ceil(WINDOW_WIDTH/32)+1):
        # for j in range(start_tilex, start_tilex+math.ceil(WINDOW_HEIGHT/32)+1):
            # here's where it gets tricky, i and j work as map coordinates to
            # find the proper tile, now just need to figure out where on the
            # image we are drawing to render the tile.
            # if (i >= 0) and (j >= 0) and (i < len(map)) and (j < len(map[0])):
                # print("rendering ", map[i][j])
                # map_image.blit(tileset[map[i][j]], (j*32, i*32))
    
    # create a 2-d list to hold the tiles of the map that we will draw
    submap = []
    for i in range(32):
        temp_row = []
        for j in range(32):
            map_row = player_map_y-16+i
            map_col = player_map_x-16+j
            if ((map_row>=0) and (map_col>=0) and (map_row<len(map)) and 
                (map_col<len(map[0]))):
                temp_row.append(map[map_row][map_col])
            else:
                temp_row.append(0)
        submap.append(temp_row)
            
    # draw the necessary part of the map
    submap_image = pygame.Surface((1024, 1024))
    for i in range(32):
        for j in range(32):
            submap_image.blit(tileset[submap[i][j]], (j*32, i*32))
    
    screen_centerx = int(WINDOW_WIDTH/2)
    screen_centery = int(WINDOW_HEIGHT/2)
    player_x_offset = player.rect.centerx-(player_map_x*32)
    player_y_offset = player.rect.centery-(player_map_y*32)
    
    # draw the map_subimage to the screen
    # maybe can modify this to take small player offset into account
    main_window.blit(submap_image, (screen_centerx-512-player_x_offset,
        screen_centery-512-player_y_offset))
    # main_window.blit(submap_image, (screen_centerx-player.rect.centerx,
        # screen_centery-player.rect.centery))
    
    # draw the map to the screen
    # main_window.blit(map_image, (0, 0))
    
    # draw the player at the center of the screen
    main_window.blit(player.image, (screen_centerx-int(player.width/2), 
        screen_centery-int(player.height/2)))
    
    # debug player x and y coordinates
    font = pygame.font.Font(None, 30)
    xstring = "x: " + str(player.rect.centerx)
    ystring = "y: " + str(player.rect.centery)
    pos_text = font.render(xstring + "   " + ystring, False, WHITE)
    main_window.blit(pos_text, (10, 10))
    offset_string = ("x offset: " + str(player_x_offset) + "   y offset: " + 
        str(player_y_offset))
    offset_text = font.render(offset_string, False, WHITE)
    main_window.blit(offset_text, (10, 30))

def main():
    game_objects = []
    keys_down = {'up': False, 'down': False, 'left': False, 'right': False}
    
    player = Player.Player()
    player.rect.centerx = 0
    player.rect.centery = 0
    game_objects.append(player)
    
    # set up the game
    pygame.init()
    main_clock = pygame.time.Clock()
    
    # create the game window
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Knight")
    
    # temporary map
    map = []
    counter = 0
    for i in range(100):
        temp_row = []
        for j in range(100):
            temp_row.append(183)
            counter += 1
        map.append(temp_row)
    
    # temporary tileset
    tileset = Image_Utils.load_tileset("src/Castle.png", 512, 512, 32, 32)
            
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
        