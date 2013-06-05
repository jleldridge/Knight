import pygame
from pygame.locals import *

ALPHA_COLOR = (255, 0, 255)

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, image, rect, attack_power, attack_force, solid=False, 
    solid_rect=None, attack_rect=None, hittable_rect=None):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = image
        self.rect = rect
        self.attack_power = attack_power
        self.attack_force = attack_force
        self.solid = solid
        if (not solid_rect) and solid:
            self.solid_rect = rect
        else:
            self.solid_rect = solid_rect
        self.attack_rect = attack_rect
        self.hittable_rect = hittable_rect

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
        attack_power = 1
        attack_force = 64
        attack_rect = rect.inflate(-5, -5)
        hittable_rect = rect.copy()
        solid_rect = attack_rect.copy()
        Enemy.__init__(self, image, rect, attack_power, attack_force, True, 
            solid_rect, attack_rect, hittable_rect)