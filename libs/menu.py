import pygame
from libs import tiles

player_tiles = tiles.TileSet("data/images/sheep_spritesheet.png", 16, 16)

def show_menu(Screen, Clock):
    temp_player_frame_count = 0
    temp_player_movement = 0
    menu_part = 0
    x = 64
    y = 64
    radius = 10
    menu_selection = 0
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
