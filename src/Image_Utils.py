def load_tileset(file, image_width, image_height, tile_width, tile_height):
    image = pygame.image.load(file).convert_alpha()
    tileset = []
    num_tiles_x = image_width/tile_width
    num_tiles_y = image_height/tile_height
    
    for i in range(num_tiles_x):
        for j in range(num_tiles_y):
            rect = (i*tile_width, j*tile_height, tile_width, tile_height)
            tileset.append(image.subsurface(rect))
    
    return tileset