import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/player.png").convert()
        self.image.set_colorkey((255, 0, 255))
        
        # get a bounding rectangle of the image
        self.rect = self.image.get_rect()
        
        self.max_x_speed = 3
        self.max_y_speed = 3
        self.x_speed = 0
        self.y_speed = 0
        
        self.health = 5

        # knockback is a counter, knocking the player back
        # max_speed * status['knockback'] pixels total over status['knockback']
        # frames
        self.knockback = 0
        self.knockback_speed = 8