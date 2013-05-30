import pygame, sys
import Player
from pygame.locals import *

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

def draw(main_window, game_objects):
    BLACK = (0, 0, 0)
    main_window.fill(BLACK)
    for o in game_objects:
        main_window.blit(o.image, o.rect)

def main():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    
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
    
    # main loop
    while True:
        # handle events
        handle_events(pygame.event.get(), keys_down)
        
        # update the game
        update_game(player, game_objects, keys_down)
        # draw game objects
        draw(main_window, game_objects)
        
        pygame.display.update()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        