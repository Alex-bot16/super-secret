"""St Andrews coastal backgrounds (levels 7–8).

Level 7: The Pier   — stone pier into North Sea, fishing boats, town skyline
Level 8: Castle Ruins — clifftop ruins, Castle Sands, bottle dungeon tower
"""
import pygame
import math

from constants import (
    WIDTH, HEIGHT, WHITE, BLACK, RED, GREY, STONE, DKGREY, BROWN, DKBROWN,
)
from backgrounds.shared import (
    sky, sea, waves, clouds, town_skyline, gradient, label,
)

_TOWN = [(40, 30, 50), (75, 25, 65), (110, 35, 45), (155, 28, 55),
         (195, 22, 40), (230, 32, 60), (270, 26, 48)]


def draw_level_7(surf):
    """The Pier – stone pier extending into the North Sea."""
    sky(surf, (105, 125, 160), (140, 155, 180))
    clouds(surf, 4, 30, 90)
    town_skyline(surf, 370, _TOWN)

    # Grass strip
    pygame.draw.rect(surf, (70, 130, 60), (0, 370, WIDTH, 40))

    # The Pier – the hero element, large and prominent
    pier_y = 400
    # Stone supports (visible below walkway)
    for px in range(560, 920, 45):
        pygame.draw.rect(surf, (120, 115, 108), (px, pier_y + 8, 10, 35))
    # Main walkway
    pygame.draw.rect(surf, (150, 145, 135), (540, pier_y, 380, 12))
    # Low walls on each side
    pygame.draw.rect(surf, (140, 135, 128), (540, pier_y - 8, 380, 8))
    pygame.draw.rect(surf, (130, 125, 118), (540, pier_y + 12, 380, 5))
    # End pillars
    pygame.draw.rect(surf, (145, 140, 130), (908, pier_y - 22, 18, 38))
    pygame.draw.rect(surf, (135, 130, 123), (905, pier_y - 26, 24, 6))
    # Start entrance
    pygame.draw.rect(surf, (145, 140, 130), (536, pier_y - 14, 16, 30))

    # Sea
    sea(surf, 430)
    waves(surf, 430, 70)

    # Fishing boats
    for bx, bc in [(350, (180, 50, 40)), (460, (40, 80, 160)), (200, (50, 140, 60))]:
        pygame.draw.ellipse(surf, bc, (bx, 445, 35, 12))
        pygame.draw.line(surf, DKBROWN, (bx + 17, 445), (bx + 17, 425), 1)

    # Seagulls
    t = pygame.time.get_ticks() / 1000
    for i, (gx, gy) in enumerate([(300, 80), (600, 60), (800, 100)]):
        gx += int(math.sin(t + i * 2) * 20)
        pygame.draw.lines(surf, WHITE, False, [(gx - 6, gy + 2), (gx, gy), (gx + 6, gy + 2)], 2)

    # Rocky shore on left
    for rx in range(0, 300, 30):
        rw = 18 + (rx * 7) % 12
        rh = 4 + (rx * 3) % 6
        pygame.draw.ellipse(surf, (95, 90, 82), (rx, 425 - rh, rw, rh * 2))

    label(surf, "St Andrews – The Pier", (200, 205, 215))


def draw_level_8(surf):
    """Castle Ruins – dramatic clifftop fortress over Castle Sands."""
    sky(surf, (95, 115, 150), (130, 145, 170))
    clouds(surf, 3, 25, 80, 70)

    # Castle ruins – dominate the background
    cx, cy = 350, 200
    s = (145, 140, 130)      # main stone
    ds = (125, 120, 110)     # darker stone
    win = (50, 50, 65)       # window openings

    # South curtain wall (longest remaining section, jagged top)
    pygame.draw.rect(surf, s, (cx, cy, 200, 130))
    jagged = [(cx, cy), (cx + 20, cy - 12), (cx + 45, cy + 5),
              (cx + 70, cy - 8), (cx + 100, cy + 6), (cx + 130, cy - 18),
              (cx + 165, cy - 5), (cx + 200, cy)]
    pygame.draw.polygon(surf, s, jagged + [(cx + 200, cy + 25), (cx, cy + 25)])
    # Wall windows
    for wx in [cx + 30, cx + 80, cx + 140]:
        pygame.draw.rect(surf, win, (wx, cy + 40, 12, 20), border_radius=2)

    # Fore Tower (left, tallest — square with crenellations)
    pygame.draw.rect(surf, s, (cx - 35, cy - 60, 45, 190))
    for i in range(0, 45, 11):
        pygame.draw.rect(surf, s, (cx - 35 + i, cy - 70, 7, 10))
    # Tower windows (narrow slits)
    pygame.draw.rect(surf, win, (cx - 20, cy - 30, 10, 20), border_radius=2)
    pygame.draw.rect(surf, win, (cx - 20, cy + 30, 10, 20), border_radius=2)
    pygame.draw.rect(surf, win, (cx - 20, cy + 80, 10, 20), border_radius=2)

    # Kitchen Tower (right, shorter — square, partially ruined)
    kt_x = cx + 190
    pygame.draw.rect(surf, s, (kt_x, cy - 10, 42, 140))
    # Ruined top edge (uneven)
    for i in range(0, 42, 8):
        cut = 5 + (i * 7) % 12
        pygame.draw.rect(surf, (105, 115, 145), (kt_x + i, cy - 10, 6, cut))
    # Crenellations on remaining section
    for i in range(0, 42, 11):
        pygame.draw.rect(surf, s, (kt_x + i, cy - 18, 7, 8))
    # Window
    pygame.draw.rect(surf, win, (kt_x + 14, cy + 30, 12, 18), border_radius=2)

    # Gate arch (centre of south wall)
    pygame.draw.rect(surf, win, (cx + 80, cy + 90, 30, 40))
    pygame.draw.ellipse(surf, win, (cx + 75, cy + 80, 40, 24))

    # Rock-cut ditch (landward defence)
    pygame.draw.rect(surf, (55, 50, 42), (cx - 55, cy + 125, 90, 10))

    # Cliff edge
    gradient(surf, (0, 330, WIDTH, 30), (110, 95, 75), (90, 80, 65))

    # Fallen rubble at cliff base
    for rx, ry in [(cx - 40, 338), (cx + 210, 342), (cx + 100, 345),
                   (cx + 160, 340), (cx - 15, 344)]:
        pygame.draw.rect(surf, ds, (rx, ry, 10 + (rx % 7), 6 + (rx % 4)))

    # Castle Sands beach
    gradient(surf, (0, 360, WIDTH, 50), (200, 190, 160), (185, 175, 145))

    # Sea
    sea(surf, 410)
    waves(surf, 410, 80)

    # Distant town right side
    town_skyline(surf, 330, [(700, 22, 40), (730, 18, 55), (758, 28, 35),
                             (795, 20, 48), (825, 25, 38)])

    label(surf, "St Andrews – Castle Ruins", (200, 205, 215))
