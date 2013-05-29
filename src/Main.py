import pygame, sys
import Player
from pygame.locals import *

def handle_events(events):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                pass
            if event.key == K_RIGHT or event.key == ord('d'):
                pass
            if event.key == K_UP or event.key == ord('w'):
                pass
            if event.key == K_DOWN or event.key == ord('s'):
                pass
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == ord('a'):
                pass
            if event.key == K_RIGHT or event.key == ord('d'):
                pass
            if event.key == K_UP or event.key == ord('w'):
                pass
            if event.key == K_DOWN or event.key == ord('s'):
                pass

def draw(main_window, objects):
    BLACK = (0, 0, 0)
    main_window.fill(BLACK)
    for o in objects:
        main_window.blit(o.image, o.rect)

def main():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    
    game_objects = []
    
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
        handle_events(pygame.event.get())
        
        # draw game objects
        draw(main_window, game_objects)
        
        pygame.display.update()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        