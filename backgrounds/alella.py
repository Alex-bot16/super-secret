"""Alella backgrounds: Village Square (4), Vineyards (5), Bodega (6)."""
import pygame
import math

from constants import (
    WIDTH, HEIGHT, WHITE, BLACK, BROWN, DKBROWN, CREAM,
    TERRACOTTA, VINE, DKGREEN, BLUE, YELLOW, RED, PINK,
)
from backgrounds.shared import (
    sky, gradient, clouds, building, pine_tree, label,
)

# ── Level 4: Village Square ──────────────────────────────────────

def draw_level_4(surf):
    """Close-up Catalan village: church tower, fountain, bougainvillea."""
    sky(surf, (255, 235, 200), (130, 180, 230))

    # Distant sea between buildings
    pygame.draw.rect(surf, (80, 150, 210), (380, 350, 180, 30))

    # Village buildings (close-up, large)
    _village_building(surf, -10, 250, 110, 160, True)
    _village_building(surf, 120, 280, 90, 130, False)
    _village_building(surf, 560, 240, 100, 170, True)
    _village_building(surf, 680, 270, 120, 140, False)
    _village_building(surf, 820, 260, 95, 150, True)
    _village_building(surf, 930, 290, 94, 120, False)

    # Church bell tower (centre-left)
    tx, ty = 250, 150
    pygame.draw.rect(surf, CREAM, (tx, ty, 50, 260))
    pygame.draw.rect(surf, (220, 210, 190), (tx, ty, 50, 260), 2)
    # Bell arch
    pygame.draw.rect(surf, (60, 50, 40), (tx + 15, ty + 15, 20, 28))
    pygame.draw.ellipse(surf, (60, 50, 40), (tx + 10, ty + 8, 30, 20))
    # Bell
    pygame.draw.circle(surf, YELLOW, (tx + 25, ty + 30), 5)
    # Cross
    pygame.draw.line(surf, (80, 70, 50), (tx + 25, ty - 20), (tx + 25, ty), 3)
    pygame.draw.line(surf, (80, 70, 50), (tx + 18, ty - 12), (tx + 32, ty - 12), 3)

    # Cobblestone ground
    gradient(surf, (0, 410, WIDTH, HEIGHT - 410), (180, 165, 140), (150, 135, 110))
    for cy in range(415, HEIGHT, 10):
        for cx in range(0, WIDTH, 14):
            off = 7 if (cy // 10) % 2 else 0
            c = (165 + (cx * 3) % 20, 150 + (cx * 7) % 15, 125 + (cx * 5) % 15)
            pygame.draw.rect(surf, c, (cx + off, cy, 12, 8), 1)

    # Stone fountain (centre)
    fx, fy = 480, 390
    pygame.draw.rect(surf, (160, 155, 145), (fx - 25, fy, 50, 20))   # basin
    pygame.draw.rect(surf, (150, 145, 135), (fx - 5, fy - 30, 10, 30))  # pillar
    pygame.draw.circle(surf, (150, 145, 135), (fx, fy - 30), 8)      # top
    # Water animation
    t = pygame.time.get_ticks() / 300
    for j in range(4):
        a = t + j * 1.57
        wx = fx + int(math.sin(a) * 10)
        wy = fy - 25 + int(math.cos(a) * 6)
        pygame.draw.circle(surf, (120, 170, 220), (wx, wy), 2)

    label(surf, "Alella – Village Square", TERRACOTTA)

def _village_building(surf, x, y, w, h, has_balcony):
    """Catalan village building with terracotta roof."""
    pygame.draw.rect(surf, CREAM, (x, y, w, HEIGHT - y))
    pygame.draw.rect(surf, (210, 200, 180), (x, y, w, HEIGHT - y), 2)
    # Terracotta roof
    pygame.draw.polygon(surf, TERRACOTTA, [
        (x - 5, y), (x + w // 2, y - 22), (x + w + 5, y)])
    # Windows
    for wy in range(y + 18, y + h - 10, 28):
        for wx in range(x + 10, x + w - 10, 24):
            pygame.draw.rect(surf, (60, 50, 40), (wx, wy, 14, 20), border_radius=2)
            pygame.draw.line(surf, (80, 70, 55), (wx + 7, wy), (wx + 7, wy + 20), 1)
    # Wrought-iron balcony
    if has_balcony and w > 50:
        by = y + 50
        pygame.draw.rect(surf, (50, 50, 55), (x + 5, by, w - 10, 3))
        for bx in range(x + 8, x + w - 8, 6):
            pygame.draw.line(surf, (50, 50, 55), (bx, by), (bx, by + 10), 1)
        # Bougainvillea
        for j in range(5):
            bfx = x + 15 + j * ((w - 30) // 5)
            pygame.draw.circle(surf, (200, 50, 130), (bfx, by + 6), 4)
            pygame.draw.circle(surf, PINK, (bfx + 3, by + 3), 3)

# ── Level 5: Vineyards ───────────────────────────────────────────

def draw_level_5(surf):
    """Terraced hillside vineyards overlooking the Mediterranean."""
    sky(surf, (100, 175, 240), (180, 215, 245))
    pygame.draw.circle(surf, (255, 230, 80), (880, 80), 50)  # sun glow
    pygame.draw.circle(surf, YELLOW, (880, 80), 40)           # sun core

    # Mediterranean sea at horizon
    gradient(surf, (0, 200, WIDTH, 50), (70, 145, 210), (90, 160, 220))
    t = pygame.time.get_ticks() / 400
    for i in range(0, WIDTH, 25):
        wy = 215 + int(math.sin(t + i * 0.12) * 2)
        pygame.draw.ellipse(surf, (100, 170, 230), (i, wy, 20, 4))

    # Far hill (covers sea's bottom edge)
    pygame.draw.polygon(surf, (110, 165, 75),
        [(0, 270), (120, 245), (300, 260), (480, 240), (660, 255),
         (820, 242), (WIDTH, 260), (WIDTH, 400), (0, 400)])
    # Masia on far hill
    pygame.draw.rect(surf, CREAM, (620, 248, 40, 22))
    pygame.draw.polygon(surf, TERRACOTTA, [(617, 248), (640, 234), (663, 248)])

    # Near hill (vineyard hill)
    pygame.draw.polygon(surf, (85, 145, 55),
        [(0, 330), (150, 305), (350, 320), (550, 298),
         (750, 315), (WIDTH, 305), (WIDTH, 520), (0, 520)])

    # Vineyard rows – indented per row so they sit on the hill
    for row in range(8):
        y = 340 + row * 22
        x_start, x_end = 30 + row * 8, WIDTH - 40 - row * 10
        for vx in range(x_start, x_end, 28):
            vx_off = vx + (row % 2) * 14
            if vx_off >= x_end: continue
            pygame.draw.line(surf, DKBROWN, (vx_off, y + 6), (vx_off, y + 14), 1)
            pygame.draw.circle(surf, VINE, (vx_off, y + 4), 5)
            pygame.draw.circle(surf, (80, 140, 45), (vx_off + 3, y + 2), 3)

    # Sandy ground below vineyard
    gradient(surf, (0, 520, WIDTH, HEIGHT - 520), (195, 180, 140), (170, 155, 115))
    # Pine trees on hill edges
    for tx, ty in [(30, 300), (200, 320), (WIDTH - 60, 310), (WIDTH - 150, 325)]:
        pine_tree(surf, tx, ty, 32)
    label(surf, "Alella – Vineyards", TERRACOTTA)

# ── Level 6: Bodega (Interior) ───────────────────────────────────

def draw_level_6(surf):
    """Interior wine cellar: stone arches, barrels, warm lamps."""
    # Dark stone walls fill entire screen
    gradient(surf, (0, 0, WIDTH, HEIGHT), (70, 60, 50), (40, 35, 28))
    # Stone brick pattern
    for by in range(0, HEIGHT, 16):
        for bx in range(0, WIDTH, 28):
            off = 14 if (by // 16) % 2 else 0
            c = (65 + (bx * 3) % 15, 55 + (bx * 7) % 12, 45 + (bx * 5) % 10)
            pygame.draw.rect(surf, c, (bx + off, by, 26, 14), 1)

    # Large stone arches across ceiling
    for ax in [160, 480, 800]:
        pygame.draw.arc(surf, (100, 90, 75), (ax - 120, 30, 240, 180), 0, math.pi, 5)
        pygame.draw.arc(surf, (85, 75, 62), (ax - 118, 32, 236, 176), 0, math.pi, 2)

    # Back wall barrels (2 rows)
    for row in range(2):
        for i in range(12):
            bx = 40 + i * 80
            by = 250 + row * 75
            _barrel(surf, bx, by)

    # Floor – darker stone
    gradient(surf, (0, 550, WIDTH, HEIGHT - 550), (55, 48, 38), (35, 30, 22))
    # Floor tiles
    for fy in range(555, HEIGHT, 20):
        for fx in range(0, WIDTH, 30):
            pygame.draw.rect(surf, (50 + (fx * 3) % 10, 43 + (fx * 7) % 8, 33), (fx, fy, 28, 18), 1)

    # Hanging warm lamps
    t = pygame.time.get_ticks() / 500
    for i, lx in enumerate([130, 340, 550, 760, 950]):
        ly = 140 + int(math.sin(t + i) * 2)
        pygame.draw.line(surf, (80, 70, 55), (lx, 0), (lx, ly), 1)
        # Lamp glow
        glow = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 200, 80, 35), (25, 25), 25)
        pygame.draw.circle(glow, (255, 220, 100, 55), (25, 25), 12)
        surf.blit(glow, (lx - 25, ly - 20))
        pygame.draw.circle(surf, (255, 210, 100), (lx, ly), 5)

    # Wine shelf on right wall
    for sy in [380, 420, 460]:
        pygame.draw.rect(surf, DKBROWN, (880, sy, 120, 4))
        for sx in range(885, 1000, 12):
            pygame.draw.rect(surf, (50, 20, 30), (sx, sy - 18, 8, 18))

    # Small window showing vineyard
    pygame.draw.rect(surf, (80, 75, 65), (20, 160, 60, 45))
    gradient(surf, (24, 164, 52, 37), (130, 180, 230), (90, 150, 60))

    label(surf, "Alella – Bodega", (180, 150, 90))

def _barrel(surf, x, y):
    pygame.draw.ellipse(surf, (100, 65, 35), (x, y, 55, 50))
    pygame.draw.ellipse(surf, (120, 80, 45), (x + 5, y + 5, 45, 40))
    # Metal bands
    pygame.draw.ellipse(surf, (80, 75, 65), (x + 2, y + 12, 51, 4), 1)
    pygame.draw.ellipse(surf, (80, 75, 65), (x + 2, y + 34, 51, 4), 1)

