import pygame
from pygame.locals import *

def load_tileset(file, image_width, image_height, tile_width, tile_height):
    image = pygame.image.load(file).convert_alpha()
    tileset = []
    num_tiles_x = int(image_width/tile_width)
    num_tiles_y = int(image_height/tile_height)
    
    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            rect = (j*tile_width, i*tile_height, tile_width, tile_height)
            tileset.append(image.subsurface(rect))
    
    return tileset