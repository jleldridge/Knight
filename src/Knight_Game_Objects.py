import pygame
from pygame.locals import *
import Tilesets

ALPHA_COLOR = (255, 0, 255)

class Knight_Game_Object:

    def __init__(self, image, pos, rect = None, solid=False, background=False):
        self.image = image
        self.rect = rect
        self.solid = solid
        if self.solid:
            self.rect = rect
        self.background = background
        
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

# definitions of game objects

class Anvil_01(Knight_Game_Object):
    
    def __init__(self, x, y):
        image = pygame.Surface((32, 32)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[133], (0,0))
        rect = image.get_rect()
        
        Knight_Game_Object.__init__(self, image, (x, y), rect, True, False)
        
        
class Bookshelf(Knight_Game_Object):
    
    def __init__(self, x, y):
        image = pygame.Surface((64, 64)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[164], (0, 0))
        image.blit(Tilesets.castle[165], (32, 0))
        image.blit(Tilesets.castle[180], (0, 32))
        image.blit(Tilesets.castle[181], (32, 32))
        rect = image.get_rect()
        
        Knight_Game_Object.__init__(self, image, (x, y), rect, True, False)

        
class Pyramid_of_crates(Knight_Game_Object):

    def __init__(self, x, y):
        image = pygame.Surface((64, 64)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[231], (0, 0))
        image.blit(Tilesets.castle[232], (32, 0))
        image.blit(Tilesets.castle[247], (0, 32))
        image.blit(Tilesets.castle[248], (32, 32))
        rect = image.get_rect()
        
        Knight_Game_Object.__init__(self, image, (x, y), rect, True, False)
        
        
class Skeleton(Knight_Game_Object):
    
    def __init__(self, x, y):
        image = pygame.Surface((32, 32)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[177], (0,0))
        rect = image.get_rect()
        
        Knight_Game_Object.__init__(self, image, (x, y), rect, False, True)
        
        
        