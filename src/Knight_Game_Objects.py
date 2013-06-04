import pygame
from pygame.locals import *
import Tilesets

ALPHA_COLOR = (255, 0, 255)

class Knight_Game_Object:

    def __init__(self, image, rect, background=False, solid=False, 
        solid_rect = None):
        
        self.image = image
        self.rect = rect
        self.solid = solid
        if self.solid:
            self.rect = rect
        self.background = background
        self.solid_rect = solid_rect

# definitions of game objects

class Anvil_01(Knight_Game_Object):
    
    def __init__(self, x, y):
        image = pygame.Surface((32, 32)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[133], (0,0))
        rect = image.get_rect()
        rect.center = (x, y)
        solid_rect = rect.inflate(-4, -16)
        solid_rect.center = (x, y+2)
        Knight_Game_Object.__init__(self, image, rect, False, True, solid_rect)
        
        
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
        rect.center = (x, y)
        solid_rect = rect.inflate(0, -32)
        solid_rect.center = (x, y+16)
        Knight_Game_Object.__init__(self, image, rect, False, True, solid_rect)

        
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
        rect.center = (x, y)
        solid_rect = rect.inflate(0, -32)
        solid_rect.center = (x, y+16)
        Knight_Game_Object.__init__(self, image, rect, False, True, solid_rect)
        
        
class Skeleton(Knight_Game_Object):
    
    def __init__(self, x, y):
        image = pygame.Surface((32, 32)).convert()
        image.fill(ALPHA_COLOR)
        image.set_colorkey(ALPHA_COLOR)
        image.blit(Tilesets.castle[177], (0,0))
        rect = image.get_rect()
        rect.center = (x, y)
        
        Knight_Game_Object.__init__(self, image, rect, True)
        
        
        