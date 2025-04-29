import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

from libs import intro, tiles, menu

sheep_tiles = tiles.TileSet("data/images/sheep_spritesheet.png", 16, 16)
pygame.display.set_icon(pygame.transform.scale(tiles.TileSet.get_tile(sheep_tiles, 0),(128,128)))

pygame.display.set_caption("Sheep flock - Intro")
intro.show_intro(screen, clock)

pygame.display.set_caption("Sheep flock - Main Menu")
menu.show_menu(screen,clock)