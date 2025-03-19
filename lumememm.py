import pygame
import math

# Pygame'i initsialiseerimine
pygame.init()

# Akna suurus
WIDTH, HEIGHT = 300, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Akna pealkiri
pygame.display.set_caption("Lumemees – Kermon Kopli")

# Värvid (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


def draw_exact_octagon(surface, color, center, size):
    """Joonistab täpse kaheksanurga (oktagoni) antud keskpunkti ja suurusega."""
    cx, cy = center
    points = []

    for i in range(8):  # Oktagoni 8 nurka
        angle = math.radians(45 * i)  # 45° sammud
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        points.append((int(x), int(y)))

    pygame.draw.polygon(surface, color, points)


# Peamine tsükkel
running = True
while running:
    screen.fill(BLACK)  # Taustavärv

    # Lumememme keha
    pygame.draw.circle(screen, WHITE, (150, 225), 50)  # Alumine osa
    pygame.draw.circle(screen, WHITE, (150, 140), 40)  # Keskmine osa
    pygame.draw.circle(screen, WHITE, (150, 75), 30)  # Pea

    # Silmad (oktagonid)
    draw_exact_octagon(screen, (0, 0, 0), (140, 70), 5)  # Vasak silm
    draw_exact_octagon(screen, (0, 0, 0), (160, 70), 5)  # Parem silm

    # Nina (kõrgemal ja teravam)
    pygame.draw.polygon(screen, RED, [(150, 95), (145, 80), (155, 80)])  # Nina kolmnurk

    # Ürituste käsitlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Uuendab ekraani

pygame.quit()