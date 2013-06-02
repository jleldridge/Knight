import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # temporarily make the player a white rectangle image
        self.width = 20
        self.height = 36
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255, 255))
        
        # get a bounding rectangle of the image
        self.rect = self.image.get_rect()
        
        self.x_speed = 3
        self.y_speed = 2