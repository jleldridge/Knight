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
        print("x: ", player.rect.centerx, " y: ", player.rect.centery)
    if keys_down['right']:
        player.rect.left += player.x_speed
        print("x: ", player.rect.centerx, " y: ", player.rect.centery)
    if keys_down['up']:
        player.rect.top -= player.y_speed
        print("x: ", player.rect.centerx, " y: ", player.rect.centery)
    if keys_down['down']:
        player.rect.top += player.y_speed
        print("x: ", player.rect.centerx, " y: ", player.rect.centery)

def draw(main_window, player, game_objects, map, tileset):
    BLACK = (0, 0, 0)
    main_window.fill(BLACK)
    
    # find which tile of the map the player is on
    player_map_x = int(player.rect.centerx/MAP_TILE_SIZE)
    player_map_y = int(player.rect.centery/MAP_TILE_SIZE)
    
    # draw the whole map
    map_image = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    start_tilex = math.floor(
        ((len(map[0])*32)-player.rect.centerx-(WINDOW_WIDTH/2))/32
    )
    start_tiley = math.floor(
        ((len(map)*32)-player.rect.centery-(WINDOW_HEIGHT/2))/32
    )
    
    for i in range(start_tiley, start_tiley+math.ceil(WINDOW_WIDTH/32)+1):
        for j in range(start_tilex, start_tilex+math.ceil(WINDOW_HEIGHT/32)+1):
            # here's where it gets tricky, i and j work as map coordinates to
            # find the proper tile, now just need to figure out where on the
            # image we are drawing to render the tile.
            map_image.blit(tileset[map[i][j]], (j*32, i*32))
    
    # draw the necessary part of the map
    # map_subimage = pygame.Surface((1024, 1024))
    # for i in range(32):
        # for j in range(32):
            # tilex = player_map_x - 16 + j
            # tiley = player_map_y - 16 + i
            # if ((tilex >= 0) and (tiley >= 0) and (tilex < len(map)) and 
                # (tiley < len(map[0]))):
                # map_subimage.blit(tileset[map[tiley][tilex]], (j*32, i*32))
    
    screen_centerx = int(WINDOW_WIDTH/2)
    screen_centery = int(WINDOW_HEIGHT/2)
    
    # draw the map_subimage to the screen
    # main_window.blit(map_subimage, (screen_centerx-player.rect.centerx,
        # screen_centery-player.rect.centery))
    
    # draw the map to the screen
    main_window.blit(map_image, (screen_centerx-player.rect.centerx, 
        screen_centery-player.rect.centery))
    
    # draw the player at the center of the screen
    main_window.blit(player.image, (screen_centerx-int(player.width/2), 
        screen_centery-int(player.height/2)))

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
    for i in range(200):
        row = []
        for j in range(200):
            row.append(183)
            counter += 1
        map.append(row)
    
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
        