"""Geneva backgrounds – one function per level.

Level 1: Lake Shore — promenade, Belle Époque buildings, sailboats, Mont Blanc
Level 2: Jet d'Eau  — 140m fountain dominates, stone jetty, mist, rainbow
Level 3: UN Quarter — Palais des Nations, Broken Chair, Avenue of Flags
"""
import pygame
import math

from constants import WIDTH, HEIGHT, WHITE, BROWN, DKBROWN, CREAM, STONE, GREY
from backgrounds.shared import (
    sky, lake, mountains, snow_caps, clouds, waves,
    building, lollipop_tree, sailboat, swan, flagpoles, label,
    gradient,
)

_PEAKS = [(350, 180, 50), (650, 200, 40), (950, 220, 35), (220, 260, 30)]


def draw_level_1(surf):
    """Lake Shore – promenade with Belle Époque buildings and sailboats."""
    sky(surf, (135, 200, 250), (185, 215, 230))
    mountains(surf, 400, (180, 190, 210))
    # Near foothills
    pts = [(0, 440), (80, 390), (200, 410), (350, 370), (500, 400),
           (650, 380), (800, 410), (1024, 430), (1024, 500), (0, 500)]
    pygame.draw.polygon(surf, (150, 165, 180), pts)
    snow_caps(surf, _PEAKS)

    lake(surf, 500)

    # Sailboats and swans
    sailboat(surf, 300, 530)
    sailboat(surf, 700, 545)
    swan(surf, 180, 520)
    swan(surf, 600, 535)

    # Stone promenade wall
    pygame.draw.rect(surf, (160, 155, 145), (0, 490, WIDTH, 12))
    pygame.draw.rect(surf, (140, 135, 125), (0, 490, WIDTH, 3))

    # Belle Époque buildings
    for bx, bw, bh in [(30, 40, 65), (78, 35, 80), (120, 45, 55),
                        (780, 38, 70), (825, 42, 60), (875, 35, 75)]:
        building(surf, bx, 490 - bh, bw, bh, CREAM, STONE)

    # Promenade trees
    for tx in [175, 220, 265, 720, 750]:
        lollipop_tree(surf, tx, 470)

    label(surf, "Geneva – Lake Shore", (200, 210, 230))


def draw_level_2(surf):
    """Jet d'Eau – 140m fountain dominates the lake."""
    sky(surf, (120, 190, 245), (175, 210, 230))
    mountains(surf, 420, (170, 180, 200))
    snow_caps(surf, _PEAKS)

    # Lake takes up more of the screen
    lake(surf, 450)

    # Distant city skyline on far shore
    for bx, bw, bh in [(40, 18, 25), (65, 14, 35), (90, 22, 28),
                        (800, 16, 30), (825, 20, 22), (855, 18, 38)]:
        pygame.draw.rect(surf, (130, 135, 145), (bx, 450 - bh, bw, bh))

    # Stone jetty extending into lake
    pygame.draw.rect(surf, STONE, (420, 520, 180, 10))
    pygame.draw.rect(surf, (140, 135, 125), (420, 518, 180, 4))

    # Jet d'Eau – the centrepiece
    t = pygame.time.get_ticks() / 400
    jx, base = 510, 450
    # Main column
    for i in range(0, 240, 2):
        spread = i * 0.015
        jitter = int(math.sin(t * 4 + i * 0.15) * spread * 2)
        bri = min(255, 240 - int(i * 0.12))
        pygame.draw.line(surf, (bri, bri, 255),
                         (jx + jitter - 1, base - i), (jx + jitter + 1, base - i), 3)
    # Spray at top
    for j in range(15):
        a = t * 3 + j * 0.45
        d = 12 + j * 3
        px = jx + int(math.sin(a) * d * 0.5)
        py = base - 240 + int(math.cos(a) * d * 0.3) - j * 2
        pygame.draw.circle(surf, (200, 220, 255), (px, py), 2)
    # Mist at base
    for j in range(10):
        mx = jx + int(math.sin(t * 2 + j) * 35)
        my = base - 3 + int(math.sin(t + j * 0.8) * 3)
        mist = pygame.Surface((24, 10), pygame.SRCALPHA)
        pygame.draw.ellipse(mist, (255, 255, 255, 40), (0, 0, 24, 10))
        surf.blit(mist, (mx - 12, my - 5))
    # Rainbow arc near spray
    for ri, rc in enumerate([(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 200, 0), (0, 100, 255)]):
        pygame.draw.arc(surf, rc, (jx - 60, base - 260 + ri * 3, 120, 60), 0, math.pi, 1)

    label(surf, "Geneva – Jet d'Eau", (200, 210, 230))


def draw_level_3(surf):
    """UN Quarter – Palais des Nations, Broken Chair, flags."""
    sky(surf, (155, 165, 180), (190, 195, 205))
    clouds(surf, 3, 30, 80, 60)

    # Ariana Park trees in background
    pygame.draw.rect(surf, (70, 120, 55), (0, 380, WIDTH, 40))
    for tx in range(30, WIDTH, 80):
        lollipop_tree(surf, tx, 365, 18, 14, (60, 110, 50))

    # Palais des Nations – large flat-roofed building
    px, py, pw, ph = 300, 260, 420, 120
    pygame.draw.rect(surf, (190, 188, 180), (px, py, pw, ph))
    pygame.draw.rect(surf, (170, 168, 160), (px, py, pw, 8))
    # Window grid
    for wy in range(py + 14, py + ph - 10, 16):
        for wx in range(px + 10, px + pw - 10, 18):
            pygame.draw.rect(surf, (100, 130, 175), (wx, wy, 12, 10))
    # Central entrance
    pygame.draw.rect(surf, (80, 80, 100), (px + pw // 2 - 15, py + ph - 35, 30, 35))
    pygame.draw.ellipse(surf, (80, 80, 100), (px + pw // 2 - 15, py + ph - 50, 30, 20))

    # Granite paving (grey ground)
    gradient(surf, (0, 420, WIDTH, HEIGHT - 420), (160, 158, 150), (130, 128, 120))

    # Avenue of Flags
    flagpoles(surf, 310, 710, 420, 20, 35)

    # Broken Chair – the iconic 12m sculpture
    cx, cy = 200, 420
    leg_w, leg_h = 8, 55
    # Three legs
    pygame.draw.rect(surf, DKBROWN, (cx - 25, cy - leg_h, leg_w, leg_h))
    pygame.draw.rect(surf, DKBROWN, (cx + 17, cy - leg_h, leg_w, leg_h))
    pygame.draw.rect(surf, DKBROWN, (cx + 17, cy - leg_h - 45, leg_w, 45))
    # Broken fourth leg (shorter, angled)
    pygame.draw.polygon(surf, DKBROWN, [
        (cx - 25, cy - leg_h - 45), (cx - 17, cy - leg_h - 45),
        (cx - 12, cy - leg_h - 20), (cx - 20, cy - leg_h - 20)])
    # Seat
    pygame.draw.rect(surf, BROWN, (cx - 30, cy - leg_h - 6, 55, 8))
    # Back
    pygame.draw.rect(surf, BROWN, (cx + 15, cy - leg_h - 80, 10, 40))
    pygame.draw.rect(surf, BROWN, (cx - 27, cy - leg_h - 80, 10, 40))
    pygame.draw.rect(surf, BROWN, (cx - 27, cy - leg_h - 82, 52, 6))

    # Ground-level water jets
    t = pygame.time.get_ticks() / 300
    for jx in range(350, 680, 50):
        jh = 8 + int(math.sin(t + jx * 0.1) * 5)
        pygame.draw.rect(surf, (120, 160, 220), (jx, 420 - jh, 4, jh))

    label(surf, "Geneva – UN Quarter", (170, 175, 185))
