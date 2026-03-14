"""St Andrews landmark backgrounds (levels 9–10).

Level 9:  The Old Course  — links landscape, Swilcan Bridge, R&A Clubhouse
Level 10: The Cathedral   — majestic ruins, St Rule's Tower, graveyard
"""
import pygame
import math

from constants import (
    WIDTH, HEIGHT, WHITE, BLACK, RED, GREY, DKGREY, STONE,
    GREEN, DKGREEN, SAND, BROWN, DKBROWN, YELLOW,
)
from backgrounds.shared import (
    sky, sea, waves, clouds, gradient, town_skyline, label,
)


def draw_level_9(surf):
    """The Old Course – wide green links, Swilcan Bridge, R&A Clubhouse."""
    # Lighter, more open sky than other St Andrews levels
    sky(surf, (140, 160, 190), (175, 190, 210))
    clouds(surf, 3, 30, 80, 50)

    # Distant sea and West Sands
    gradient(surf, (0, 180, WIDTH, 40), (90, 145, 190), (100, 155, 200))

    # R&A Clubhouse – iconic grey stone building behind 18th green
    rx, ry = 700, 200
    pygame.draw.rect(surf, (155, 150, 140), (rx, ry, 100, 60))
    pygame.draw.rect(surf, (140, 135, 125), (rx, ry, 100, 8))
    # Windows (distinctive large)
    for wx in range(rx + 10, rx + 90, 20):
        pygame.draw.rect(surf, (80, 90, 110), (wx, ry + 16, 14, 18))
        pygame.draw.rect(surf, (80, 90, 110), (wx, ry + 40, 14, 14))
    # Flag on roof
    pygame.draw.line(surf, DKGREY, (rx + 50, ry), (rx + 50, ry - 20), 2)
    pygame.draw.rect(surf, (180, 30, 30), (rx + 50, ry - 20, 12, 7))

    # Town buildings behind
    town_skyline(surf, 255, [(30, 22, 40), (60, 18, 55), (85, 28, 35),
                             (850, 20, 45), (880, 25, 38), (915, 22, 50)])

    # Golden rough grass (sides)
    gradient(surf, (0, 260, WIDTH, HEIGHT - 260), (180, 170, 120), (155, 145, 100))

    # Wide green fairway sweeping across
    pts = [(0, 350), (100, 320), (300, 330), (500, 310), (700, 300),
           (900, 320), (WIDTH, 340), (WIDTH, 500), (0, 500)]
    pygame.draw.polygon(surf, (80, 150, 65), pts)

    # Putting greens
    pygame.draw.ellipse(surf, (70, 160, 55), (550, 340, 80, 28))
    pygame.draw.ellipse(surf, (70, 160, 55), (200, 370, 60, 22))

    # Sand bunkers
    for bx, by, bw in [(310, 360, 35), (630, 355, 30), (480, 390, 25)]:
        pygame.draw.ellipse(surf, SAND, (bx, by, bw, 12))
        pygame.draw.ellipse(surf, (175, 160, 120), (bx, by - 2, bw, 5))

    # Swilcan Burn (stream)
    pygame.draw.line(surf, (80, 110, 140), (330, 400), (530, 380), 3)
    t = pygame.time.get_ticks() / 400
    for i in range(330, 530, 20):
        wy = 398 - int((530 - i) * 0.04) + int(math.sin(t + i * 0.1) * 2)
        pygame.draw.circle(surf, (90, 120, 155), (i, wy), 3)

    # Swilcan Bridge – iconic stone humpback
    bx, by = 420, 388
    pygame.draw.arc(surf, STONE, (bx - 15, by - 12, 30, 24), 0, math.pi, 4)
    pygame.draw.rect(surf, STONE, (bx - 15, by, 30, 5))
    pygame.draw.rect(surf, (140, 135, 125), (bx - 17, by, 4, 8))
    pygame.draw.rect(surf, (140, 135, 125), (bx + 13, by, 4, 8))

    # Flagsticks
    for fx, fy, fc in [(590, 340, RED), (230, 370, YELLOW)]:
        pygame.draw.line(surf, BLACK, (fx, fy), (fx, fy - 28), 2)
        pygame.draw.polygon(surf, fc, [(fx, fy - 28), (fx + 12, fy - 24), (fx, fy - 20)])

    label(surf, "St Andrews – The Old Course", (180, 185, 195))


def draw_level_10(surf):
    """The Cathedral – Scotland's largest, now a magnificent ruin."""
    # Dramatic dark sky
    sky(surf, (85, 100, 135), (110, 120, 145))
    clouds(surf, 4, 20, 70, 80)

    # Sea visible behind, dark and moody
    sea(surf, 180, (50, 80, 125), (35, 65, 105))
    waves(surf, 180, 40, (65, 95, 140))

    s = (140, 136, 126)     # main stone
    ds = (120, 116, 106)    # darker stone
    win = (50, 50, 65)      # window openings

    # ── East gable (tallest remaining wall) ──
    gx, gy = 350, 100
    pygame.draw.rect(surf, s, (gx, gy, 100, 180))
    # Large pointed window opening (sky shows through)
    pygame.draw.rect(surf, (95, 108, 140), (gx + 30, gy + 20, 40, 80))
    pygame.draw.polygon(surf, (95, 108, 140), [(gx + 30, gy + 20), (gx + 50, gy - 5), (gx + 70, gy + 20)])
    # Stone tracery in window
    pygame.draw.line(surf, s, (gx + 50, gy - 5), (gx + 50, gy + 100), 2)
    pygame.draw.line(surf, s, (gx + 30, gy + 50), (gx + 70, gy + 50), 1)
    # Corner turrets
    pygame.draw.rect(surf, ds, (gx - 12, gy - 20, 18, 200))
    pygame.draw.rect(surf, ds, (gx + 94, gy - 20, 18, 200))
    # Turret tops (crenellations)
    for tx in [gx - 12, gx + 94]:
        for i in range(0, 18, 6):
            pygame.draw.rect(surf, ds, (tx + i, gy - 28, 4, 8))

    # ── St Rule's Tower (tall, separate, distinctive) ──
    tx, ty = 540, 80
    pygame.draw.rect(surf, s, (tx, ty, 28, 200))
    pygame.draw.rect(surf, ds, (tx, ty, 28, 6))
    # Small windows
    pygame.draw.rect(surf, win, (tx + 10, ty + 30, 8, 14))
    pygame.draw.rect(surf, win, (tx + 10, ty + 80, 8, 14))
    pygame.draw.rect(surf, win, (tx + 10, ty + 130, 8, 14))

    # ── Ruined nave walls ──
    for wx, ww, wh in [(450, 80, 60), (225, 70, 45), (260, 55, 70)]:
        pygame.draw.rect(surf, s, (wx, 280 - wh, ww, wh))
        # Irregular broken top
        for i in range(0, ww, 8):
            cut = (i * 7) % 12
            pygame.draw.rect(surf, (95, 108, 140), (wx + i, 280 - wh - 2, 6, cut))

    # ── Precinct wall ──
    pygame.draw.rect(surf, (130, 126, 116), (0, 290, WIDTH, 12))

    # ── Graveyard ──
    gradient(surf, (0, 302, WIDTH, 100), (65, 110, 55), (50, 90, 42))
    # Headstones
    for hx in range(40, WIDTH - 40, 35):
        hh = 12 + (hx * 3) % 10
        tilt = (hx * 7) % 5 - 2
        pygame.draw.rect(surf, (130, 125, 115),
                         (hx + tilt, 370 - hh, 10, hh), border_radius=2)

    # ── Ground and coast ──
    gradient(surf, (0, 400, WIDTH, HEIGHT - 400), (75, 120, 60), (55, 95, 145))
    waves(surf, 500, 50)

    # Flying buttress on west front
    pygame.draw.line(surf, s, (225, 260), (200, 285), 4)
    pygame.draw.rect(surf, s, (215, 235, 18, 55))

    # Scattered rubble
    for rx, ry in [(300, 285), (470, 288), (380, 290), (550, 292)]:
        pygame.draw.rect(surf, ds, (rx, ry, 10, 6))

    # Crows
    t = pygame.time.get_ticks() / 800
    for i, (cx, cy) in enumerate([(280, 50), (500, 35), (680, 55)]):
        cx += int(math.sin(t + i * 2.5) * 25)
        pygame.draw.lines(surf, BLACK, False, [(cx - 5, cy + 2), (cx, cy), (cx + 5, cy + 2)], 2)

    label(surf, "St Andrews – The Cathedral", (190, 195, 205))
