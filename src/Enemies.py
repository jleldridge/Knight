import pygame
from pygame.locals import *

ALPHA_COLOR = (255, 0, 255)

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, image, rect):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = rect

# Enemy definitions

class Slime(Enemy):
    
    def __init__(self, x, y):
        # slime will temporarily be a green square
        image = pygame.Surface((32, 32)).convert()
        image.fill((0, 255, 30))
        image.set_colorkey(ALPHA_COLOR)
        rect = image.get_rect()
        rect.centerx = x
        rect.centery = y
        Enemy.__init__(self, image, rect)