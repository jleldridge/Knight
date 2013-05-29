import pygame, sys
import Player
from pygame.locals import *

def main():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    
    BLACK = (0, 0, 0)
    
    player = Player.Player()
    player.rect.x = 800/2
    player.rect.y = 600/2
    
    # set up the game
    pygame.init()
    main_clock = pygame.time.Clock()
    
    # create the game window
    main_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption("Knight")
    
    # main loop
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # clear the screen
        main_window.fill(BLACK)
        
        main_window.blit(player.image, player.rect)
        
        pygame.display.update()
        main_clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    except:
        raise
        