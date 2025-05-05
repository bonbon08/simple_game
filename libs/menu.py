import pygame
from libs import tiles
from libs.objects import player
player_tiles = tiles.TileSet("data/images/player_spritesheet.png", 16, 16)

def show_menu(Screen, Clock):
    player_obj = player.Player(0,0,0,0,288,208,0, player_tiles)
    radius = 1
    menu_selection = 0
    menu_part = 0
    run_menu = True
    radiusaddsize = 1
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
        Screen.fill("white") # Temp background

        keys = pygame.key.get_pressed()
        match menu_part:
            case 0:
                player_obj.frame = player_obj.player_spritesheet.get_tile_scalled(player_obj.frame_count, (64,64))
                Screen.blit(player_obj.frame, (player_obj.x, player_obj.y))
                mask = pygame.Surface((640, 480), pygame.SRCALPHA)
                mask.fill((0, 0, 0, 255))
                pygame.draw.circle(mask, (0, 0, 0, 0), (320, 240), round(radius))
                Screen.blit(mask, (0,0))
                radius += radiusaddsize 
                radiusaddsize += 0.1
                if radius >= int((640**2 + 480**2)**0.5)+5:
                    menu_part = 1
            case 1:
                player_obj.move(keys)
                Screen.blit(player_obj.frame, (player_obj.x, player_obj.y))

        pygame.display.flip()
        Clock.tick(60)
