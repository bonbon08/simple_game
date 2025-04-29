import pygame
from libs import tiles
from libs.objects import player
player_tiles = tiles.TileSet("data/images/player_spritesheet.png", 16, 16)

def show_menu(Screen, Clock):
    player_obj = player.Player(0,0,0,0,288,208)
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
                player_sprite = player_tiles.get_tile_scalled(player_obj.frame_count, (64,64))
                Screen.blit(player_sprite, (player_obj.x, player_obj.y))
                mask = pygame.Surface((640, 480), pygame.SRCALPHA)
                mask.fill((0, 0, 0, 255))
                pygame.draw.circle(mask, (0, 0, 0, 0), (320, 240), round(radius))
                Screen.blit(mask, (0,0))
                radius += radiusaddsize 
                radiusaddsize += 0.1
                if radius >= int((640**2 + 480**2)**0.5)+5:
                    menu_part = 1
            case 1:
                player_obj.pre_movement = player_obj.movement
                player_obj.movement = 0
                if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    player_obj.y -= 4
                    player_obj.movement = 1
                elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                    player_obj.y += 4
                    player_obj.movement = 2
                else:
                    player_obj.movement = 0
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    player_obj.x -= 4
                    player_obj.movement = 3
                    player_sprite = pygame.transform.flip(player_tiles.get_tile_scalled(player_obj.frame_count, (64,64)), True, False)
                elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                    player_obj.x += 4
                    player_obj.movement = 4
                    player_sprite = player_tiles.get_tile_scalled(player_obj.frame_count, (64,64))
                if player_obj.pre_movement == player_obj.movement and player_obj.movement != 0:
                    player_obj.sub_frame_count += 1
                    print(player_obj.frame_count, player_obj.movement, player_obj.pre_movement, player_obj.sub_frame_count)
                    if player_obj.sub_frame_count == 4:
                        player_obj.frame_count += 1
                        player_obj.sub_frame_count = 0
                    if player_obj.frame_count == 7:
                        player_obj.frame_count = 1
                else:
                    player_obj.frame_count = 0
                    player_sprite = player_tiles.get_tile_scalled(player_obj.frame_count, (64,64))
                    print(player_obj.frame_count, player_obj.movement, player_obj.pre_movement, player_obj.sub_frame_count)
                    player_obj.sub_frame_count = 0
                Screen.blit(player_sprite, (player_obj.x, player_obj.y))

        pygame.display.flip()
        Clock.tick(60)
