import pygame
import sys

pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Hintergrundbild laden
background = pygame.image.load("data/images/ground_spritesheet.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Kreis-Startposition in der Mitte und Radius
center_x, center_y = WIDTH // 2, HEIGHT // 2
radius = 10
max_radius = int((WIDTH**2 + HEIGHT**2)**0.5)
expand_rate = 5

# Spielerparameter
player_radius = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Spielstatus
reveal_done = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not reveal_done:
        # Hintergrund und Maske
        screen.blit(background, (0, 0))

        # Schwarze Maske mit transparentem Kreis in der Mitte
        mask = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        mask.fill((0, 0, 0, 255))
        pygame.draw.circle(mask, (0, 0, 0, 0), (center_x, center_y), radius)
        screen.blit(mask, (0, 0))

        # Radius vergrößern
        radius += expand_rate
        if radius >= max_radius:
            reveal_done = True
    else:
        # Vollständiger Hintergrund
        screen.blit(background, (0, 0))

        # Spielerbewegung
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Spieler zeichnen
        pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), player_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
