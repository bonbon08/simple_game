import pygame
from libs import tiles

player_tiles = tiles.TileSet("data/images/player_spritesheet.png", 16, 16)

def show_menu(Screen, Clock):
    temp_player_sub_frame_count = 0
    temp_player_frame_count = 0
    temp_player_movement = 0
    temp_player_pre_movement = 0
    menu_part = 0
    x = 288
    y = 208
    radius = 1
    menu_selection = 0
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
                player_sprite = player_tiles.get_tile_scalled(temp_player_frame_count, (64,64))
                Screen.blit(player_sprite, (x, y))
                mask = pygame.Surface((640, 480), pygame.SRCALPHA)
                mask.fill((0, 0, 0, 255))
                pygame.draw.circle(mask, (0, 0, 0, 0), (320, 240), round(radius))
                Screen.blit(mask, (0,0))
                radius += radiusaddsize 
                radiusaddsize += 0.1
                if radius >= int((640**2 + 480**2)**0.5)+5:
                    menu_part = 1
            case 1:
                temp_player_pre_movement = temp_player_movement
                temp_player_movement = 0
                if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    y -= 4
                    temp_player_movement = 1
                elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                    y += 4
                    temp_player_movement = 2
                else:
                    temp_player_movement = 0
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    x -= 4
                    temp_player_movement = 3
                    player_sprite = pygame.transform.flip(player_tiles.get_tile_scalled(temp_player_frame_count, (64,64)), True, False)
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    x += 4
                    temp_player_movement = 4
                    player_sprite = player_tiles.get_tile_scalled(temp_player_frame_count, (64,64))
                if temp_player_pre_movement == temp_player_movement and temp_player_movement != 0:
                    temp_player_sub_frame_count += 1
                    print(temp_player_frame_count, temp_player_movement, temp_player_pre_movement, temp_player_sub_frame_count)
                    if temp_player_sub_frame_count == 4:
                        temp_player_frame_count += 1
                        temp_player_sub_frame_count = 0
                    if temp_player_frame_count == 7:
                        temp_player_frame_count = 1
                else:
                    temp_player_frame_count = 0
                    player_sprite = player_tiles.get_tile_scalled(temp_player_frame_count, (64,64))
                    print(temp_player_frame_count, temp_player_movement, temp_player_pre_movement, temp_player_sub_frame_count)
                    temp_player_sub_frame_count = 0
                Screen.blit(player_sprite, (x, y))

        pygame.display.flip()
        Clock.tick(60)
