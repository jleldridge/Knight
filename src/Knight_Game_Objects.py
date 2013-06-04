import pygame
from pygame.locals import *
import Tilesets

class Knight_Game_Object:

    def __init__(self, image, solid=False, rect = None):
        self.image = image
        self.rect = rect
        self.solid = solid
        if self.solid:
            self.rect = rect

# definitions of game objects

# Pyramid of crates
image = pygame.Surface((64, 64)).convert()
image.fill((255,255,255))
image.set_colorkey((255,255,255))
image.blit(Tilesets.castle[231], (0, 0))
image.blit(Tilesets.castle[232], (32, 0))
image.blit(Tilesets.castle[247], (0, 32))
image.blit(Tilesets.castle[248], (32, 32))
rect = image.get_rect()
pyramid_of_crates = Knight_Game_Object(image, True, rect)
