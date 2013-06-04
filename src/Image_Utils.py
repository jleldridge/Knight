import pygame, sys
from pygame.locals import *

def load_tileset(file, image_width, image_height, tile_width, tile_height, colorkey):
    image = pygame.image.load(file).convert()
    tileset = []
    num_tiles_x = int(image_width/tile_width)
    num_tiles_y = int(image_height/tile_height)
    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            rect = (j*tile_width, i*tile_height, tile_width, tile_height)
            temp_tile = image.subsurface(rect).convert()
            temp_tile.set_colorkey(colorkey)
            tileset.append(temp_tile)
    
    return tileset