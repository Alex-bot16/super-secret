"""Shared drawing helpers used by all background painters."""
import pygame
import math

from constants import (
    WIDTH, HEIGHT, WHITE, BLACK, GREY, DKGREY, RED, GREEN, DKGREEN,
    BROWN, DKBROWN, STONE, CREAM, SAND, TERRACOTTA, GOLD,
)


# ── Gradients ─────────────────────────────────────────────────────

def gradient(surf, rect, top, bottom):
    """Vertical gradient fill inside *rect*."""
    x, y, w, h = rect
    for row in range(h):
        ratio = row / max(1, h - 1)
        c = [int(top[i] + (bottom[i] - top[i]) * ratio) for i in range(3)]
        pygame.draw.line(surf, c, (x, y + row), (x + w, y + row))


def sky(surf, top, bottom):
    """Fill full screen with a sky gradient."""
    gradient(surf, (0, 0, WIDTH, HEIGHT), top, bottom)


# ── Water ─────────────────────────────────────────────────────────

def sea(surf, y, top_col=(55, 95, 145), bot_col=(35, 70, 110)):
    """Sea gradient from y to bottom of screen."""
    gradient(surf, (0, y, WIDTH, HEIGHT - y), top_col, bot_col)


def waves(surf, y, depth=70, colour=(75, 115, 165)):
    """Animated wave crests starting at y."""
    t = pygame.time.get_ticks() / 350
    for row in range(y, min(y + depth, HEIGHT), 13):
        for i in range(0, WIDTH, 22):
            wy = row + int(math.sin(t + i * 0.14 + row * 0.04) * 3)
            pygame.draw.ellipse(surf, colour, (i, wy, 19, 4))


def lake(surf, y, top=(70, 140, 210), bot=(40, 100, 170)):
    """Lake gradient + waves."""
    gradient(surf, (0, y, WIDTH, HEIGHT - y), top, bot)
    waves(surf, y, 70, (90, 160, 235))


# ── Clouds ────────────────────────────────────────────────────────

def clouds(surf, count=4, y_lo=40, y_hi=110, alpha=90):
    """Drifting semi-transparent clouds."""
    t = pygame.time.get_ticks() / 2500
    seeds = [(150, 55, 110), (400, 85, 85), (700, 45, 125), (920, 100, 75)]
    for i in range(min(count, len(seeds))):
        cx, cy, cw = seeds[i]
        cy = max(y_lo, min(y_hi, cy))
        drift = int(math.sin(t + i * 1.3) * 18)
        s = pygame.Surface((cw, 32), pygame.SRCALPHA)
        pygame.draw.ellipse(s, (220, 225, 235, alpha), (0, 8, cw, 18))
        pygame.draw.ellipse(s, (230, 235, 245, alpha - 20), (cw // 5, 0, cw * 3 // 5, 26))
        surf.blit(s, (cx + drift, cy))


# ── Mountains ─────────────────────────────────────────────────────

def mountains(surf, y_base=400, colour=(180, 190, 210)):
    """Jagged mountain silhouette."""
    pts = [(0, y_base), (60, y_base-90), (140, y_base-60), (220, y_base-140),
           (350, y_base-220), (450, y_base-150), (580, y_base-180),
           (650, y_base-200), (800, y_base-140), (950, y_base-180),
           (WIDTH, y_base-100), (WIDTH, y_base+100), (0, y_base+100)]
    pygame.draw.polygon(surf, colour, pts)


def snow_caps(surf, peaks):
    """Snow triangles.  peaks = [(x, y, width), ...]"""
    for px, py, w in peaks:
        pygame.draw.polygon(surf, WHITE, [(px, py), (px - w, py + w), (px + w, py + w)])


# ── Buildings ─────────────────────────────────────────────────────

def building(surf, x, y, w, h, wall=CREAM, roof=STONE):
    """Simple building with windows and peaked roof."""
    pygame.draw.rect(surf, wall, (x, y, w, h))
    for wy in range(y + 8, y + h - 6, 14):
        for wx in range(x + 5, x + w - 5, 12):
            pygame.draw.rect(surf, (50, 50, 70), (wx, wy, 6, 9))
    pygame.draw.polygon(surf, roof, [
        (x - 3, y), (x + w // 2, y - int(h * 0.3)), (x + w + 3, y)])


def town_skyline(surf, y, buildings_data, wall=(140, 138, 130), roof=(120, 115, 108)):
    """Row of buildings.  buildings_data = [(x, w, h), ...]"""
    for bx, bw, bh in buildings_data:
        pygame.draw.rect(surf, wall, (bx, y - bh, bw, bh))
        pygame.draw.polygon(surf, roof, [
            (bx - 3, y - bh), (bx + bw // 2, y - bh - 14), (bx + bw + 3, y - bh)])
        pygame.draw.rect(surf, (110, 108, 100), (bx + bw - 10, y - bh - 16, 6, 16))
        for wy in range(y - bh + 8, y - 5, 12):
            for wx in range(bx + 4, bx + bw - 4, 10):
                pygame.draw.rect(surf, (80, 85, 100), (wx, wy, 5, 7))
                if (wx + wy) % 3 == 0:
                    pygame.draw.rect(surf, (200, 180, 100), (wx + 1, wy + 1, 3, 5))


# ── Trees & nature ────────────────────────────────────────────────

def lollipop_tree(surf, x, y, trunk_h=20, radius=12, colour=DKGREEN):
    """Simple circle-on-stick tree."""
    pygame.draw.rect(surf, BROWN, (x - 2, y, 4, trunk_h))
    pygame.draw.circle(surf, colour, (x, y - radius + 4), radius)


def pine_tree(surf, x, y, h=30, colour=DKGREEN):
    """Triangle pine tree."""
    pygame.draw.rect(surf, DKBROWN, (x - 2, y, 4, h // 3))
    pygame.draw.polygon(surf, colour, [(x, y - h), (x - h // 3, y), (x + h // 3, y)])


# ── Flags ─────────────────────────────────────────────────────────

def flagpoles(surf, x_start, x_end, y, spacing=22, pole_h=28):
    """Row of flagpoles with random-coloured flags."""
    flag_colours = [(200, 50, 50), (50, 50, 200), (50, 180, 50),
                    (200, 200, 50), (200, 100, 50), (150, 50, 150)]
    for i, fx in enumerate(range(x_start, x_end, spacing)):
        pygame.draw.line(surf, GREY, (fx, y), (fx, y - pole_h), 1)
        c = flag_colours[i % len(flag_colours)]
        pygame.draw.rect(surf, c, (fx, y - pole_h, 8, 5))


# ── Misc ──────────────────────────────────────────────────────────

def label(surf, text, colour, x=80, y=20, size=16):
    """Small city name label."""
    from utils import draw_text
    draw_text(surf, text, size, colour, x, y)


def sailboat(surf, x, y):
    """Tiny sailboat."""
    pygame.draw.polygon(surf, WHITE, [(x, y - 15), (x, y), (x + 8, y)])
    pygame.draw.rect(surf, DKBROWN, (x - 8, y, 20, 4))


def swan(surf, x, y):
    """Tiny swan shape."""
    pygame.draw.ellipse(surf, WHITE, (x, y, 12, 6))
    pygame.draw.arc(surf, WHITE, (x + 8, y - 8, 8, 12), 0, math.pi, 2)
