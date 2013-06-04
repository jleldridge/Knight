def create_tileset_cheatsheet(file, image_width, image_height, tile_width, tile_height):
    pygame.init()
    window = pygame.display.set_mode((200, 200), 0, 32)
    
    image = pygame.image.load(file).convert_alpha()
    tileset = []
    num_tiles_x = int(image_width/tile_width)
    num_tiles_y = int(image_height/tile_height)
    counter = 0
    font = pygame.font.Font(None, 15)
    for i in range(num_tiles_y):
        for j in range(num_tiles_x):
            num_string = str(counter)
            num_text = font.render(num_string, True, (255, 255, 255))
            image.blit(num_text, (j*tile_width+5, i*tile_height+5))
            counter += 1
    file_name = file[:-4] + "cheatsheet" + file[-4:]
    pygame.image.save(image, file_name)
    
    pygame.quit()
    sys.exit()