import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # temporarily make the player a white rectangle image
        self.width = 21
        self.height = 40
        self.image = pygame.image.load("src/player.png").convert()
        self.image.set_colorkey((255, 0, 255))
        
        # get a bounding rectangle of the image
        self.rect = self.image.get_rect()
        
        self.x_speed = 3
        self.y_speed = 2