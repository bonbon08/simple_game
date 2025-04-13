import pygame
from libs import tiles

sheep_tiles = tiles.TileSet("data/images/intro/sheep_spritesheet.png", 16, 16)

def show_intro(Screen, Clock):
    temp_sheep_tile_count = -5
    running = True
    x = -64
    y = 160
    scale_x = 64
    scale_y = 64
    intro_part = 0
    fade_max = 100
    fade = fade_max
    font = pygame.font.SysFont(None, 48)
    top_text = font.render('Sheep flock', True, "WHITE")
    bottom_text = font.render('by Bonbon', True, "WHITE")
    while running:
        for user_action in pygame.event.get():
            if user_action.type == pygame.QUIT:
                running = True
                print("Game shut down")
                pygame.quit()
        if temp_sheep_tile_count >= 85:
            temp_sheep_tile_count = -5
        temp_sheep = pygame.transform.scale(sheep_tiles.get_tile(round(temp_sheep_tile_count/10)), (scale_x,scale_y))
        
        top_text.set_alpha(min(1.0,fade/fade_max)*255)
        bottom_text.set_alpha(min(1.0,fade/fade_max)*255)
        temp_sheep.set_alpha(min(1.0,fade/fade_max)*255)
        
        Screen.fill("black")
        Screen.blit(temp_sheep, (x,y))
        match intro_part:
            case 0:
                x += 4
                temp_sheep_tile_count += 4
                if x >= 288:
                    temp_sheep_tile_count = 0
                    intro_part = 1
            case 1:
                x -= 1
                y -= 1
                scale_x += 2
                scale_y += 2
                if scale_x >= 240:
                    timer = 0
                    intro_part = 2
            case 2:
                timer += 1
                Screen.blit(top_text, (230, 20))
                Screen.blit(bottom_text, (230, 380))
                if timer == 120:
                    intro_part = 3
            case 3:
                Screen.blit(top_text, (230, 20))
                Screen.blit(bottom_text, (230, 380))
                fade -= 1
                if fade == 0:
                    running = False
        pygame.display.flip()
        Clock.tick(60)