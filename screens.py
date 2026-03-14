"""
screens.py – Menu, level-complete, and game-complete screen drawing.

Each function takes the screen surface plus whatever state it needs.
"""
import pygame
import math
import random

from constants import (
    WIDTH, HEIGHT,
    WHITE, BLACK, GREY, PINK, BLUE, GOLD, CREAM, LTBLUE,
    GREEN, CYAN, ORANGE, PURPLE, RED, YELLOW,
)
from utils import draw_text
from player import Player


# ── Menu ──────────────────────────────────────────────────────────

def draw_menu(screen, current_level, girl_controls, boy_controls):
    """Full menu screen with title, characters, and level selector."""
    screen.fill((20, 20, 40))
    t = pygame.time.get_ticks() / 1000

    _draw_stars(screen, t)
    _draw_title(screen, t)
    _draw_characters(screen, girl_controls, boy_controls)
    _draw_level_selector(screen, current_level, t)


def _draw_stars(screen, t):
    random.seed(42)
    for _ in range(60):
        sx = random.randint(0, WIDTH)
        sy = random.randint(0, HEIGHT // 2)
        bri = int(150 + 100 * math.sin(t * 2 + sx))
        pygame.draw.circle(screen, (bri, bri, bri), (sx, sy), 1)


def _draw_title(screen, t):
    bob = int(math.sin(t * 2) * 8)
    draw_text(screen, "Canvas & Code", 64, GOLD, WIDTH // 2, 150 + bob)
    draw_text(screen, "A Cooperative Adventure", 24, CREAM, WIDTH // 2, 210 + bob)


def _draw_characters(screen, girl_controls, boy_controls):
    gx, gy = WIDTH // 2 - 80, 320
    bx, by = WIDTH // 2 + 60, 320
    Player(gx, gy, girl_controls, PINK, "Girl", "art").draw(screen)
    Player(bx, by, boy_controls, BLUE, "Boy", "tech").draw(screen)
    draw_text(screen, "WASD", 14, PINK, gx + 14, gy + 50)
    draw_text(screen, "Collect: Canvas + Brush", 11, PINK, gx + 14, gy + 68)
    draw_text(screen, "ARROWS", 14, BLUE, bx + 14, by + 50)
    draw_text(screen, "Collect: Computer", 11, BLUE, bx + 14, by + 68)


def _draw_level_selector(screen, level, t):
    draw_text(screen, f"Level {level} / 10", 28, WHITE, WIDTH // 2, 450)
    draw_text(screen, "< >  to select level", 16, GREY, WIDTH // 2, 490)
    loc = {1: "Geneva", 2: "Geneva", 3: "Geneva",
           4: "Alella", 5: "Alella", 6: "Alella"}.get(level, "St Andrews")
    region = {"Geneva": "Switzerland", "Alella": "Spain", "St Andrews": "Scotland"}[loc]
    draw_text(screen, f"{loc}, {region}", 20, LTBLUE, WIDTH // 2, 530)
    pulse = int(200 + 55 * math.sin(t * 4))
    draw_text(screen, "Press ENTER to start", 22, (pulse, pulse, pulse), WIDTH // 2, 620)
    draw_text(screen, "ESC to quit", 14, GREY, WIDTH // 2, 660)


# ── Level complete ────────────────────────────────────────────────

def draw_level_complete(screen, level_num, title, timer):
    """Celebration screen after completing a level."""
    screen.fill((20, 30, 50))
    t = pygame.time.get_ticks() / 1000
    draw_text(screen, "Level Complete!", 52, GOLD, WIDTH // 2, HEIGHT // 2 - 60)
    draw_text(screen, f"Level {level_num} – {title}", 24, WHITE, WIDTH // 2, HEIGHT // 2)
    _firework_ring(screen, t)
    if timer > 60:
        pulse = int(200 + 55 * math.sin(t * 4))
        draw_text(screen, "Press ENTER for next level", 20,
                  (pulse, pulse, pulse), WIDTH // 2, HEIGHT // 2 + 80)


# ── Game complete ─────────────────────────────────────────────────

def draw_game_complete(screen):
    """Final celebration after all 10 levels."""
    screen.fill((10, 10, 30))
    t = pygame.time.get_ticks() / 1000
    _firework_burst(screen, t)
    draw_text(screen, "Congratulations!", 60, GOLD, WIDTH // 2, HEIGHT // 2 - 100)
    draw_text(screen, "You completed all 10 levels!", 28, WHITE, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text(screen, "Geneva · Alella · St Andrews", 22, LTBLUE, WIDTH // 2, HEIGHT // 2 + 20)
    draw_text(screen, "Canvas & Code – Together!", 24, PINK, WIDTH // 2, HEIGHT // 2 + 70)
    pulse = int(200 + 55 * math.sin(t * 4))
    draw_text(screen, "Press ENTER to return to menu", 18,
              (pulse, pulse, pulse), WIDTH // 2, HEIGHT // 2 + 140)


# ── Firework helpers ──────────────────────────────────────────────

_FW_COLOURS = [GOLD, PINK, CYAN, ORANGE, GREEN, PURPLE, RED, YELLOW]

def _firework_ring(screen, t):
    for i in range(8):
        a = t * 3 + i * 0.8
        fx = WIDTH // 2 + int(math.cos(a) * 150)
        fy = HEIGHT // 2 + int(math.sin(a) * 80)
        pygame.draw.circle(screen, _FW_COLOURS[i % 8], (fx, fy), 6)

def _firework_burst(screen, t):
    random.seed(int(t * 2))
    for _ in range(20):
        fx = random.randint(50, WIDTH - 50)
        fy = random.randint(50, HEIGHT // 2)
        pygame.draw.circle(screen, random.choice(_FW_COLOURS), (fx, fy), random.randint(3, 8))
