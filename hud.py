"""hud.py – In-game HUD panels and bottom bar.

All functions take the screen surface + the game state they need.
"""
import pygame

from constants import (
    WIDTH, HEIGHT, WHITE, GREY, DKGREY, GREEN, PINK, BLUE,
    CYAN, ORANGE, RED, DKBROWN,
)
from utils import draw_text, draw_text_left


# ── Panels ────────────────────────────────────────────────────────

def draw_hud(screen, girl, boy, girl_done, boy_done):
    """Draw both player panels."""
    _draw_girl_panel(screen, girl, girl_done)
    _draw_boy_panel(screen, boy, boy_done)


def _draw_panel(screen, x, y, w, h, border_colour):
    panel = pygame.Surface((w, h), pygame.SRCALPHA)
    panel.fill((0, 0, 0, 170))
    pygame.draw.rect(panel, border_colour, (0, 0, w, h), 2, border_radius=6)
    screen.blit(panel, (x, y))


def _draw_girl_panel(screen, girl, girl_done):
    _draw_panel(screen, 8, 8, 230, 72, PINK)
    draw_text_left(screen, "Girl  (WASD)", 15, PINK, 16, 12)
    _item_status(screen, 18,  36, "Canvas", 'canvas' in girl.collected, _mini_canvas)
    _item_status(screen, 130, 36, "Brush",  'paintbrush' in girl.collected, _mini_brush)
    if girl_done:
        draw_text_left(screen, ">> Go to door!", 13, GREEN, 18, 56)


def _draw_boy_panel(screen, boy, boy_done):
    rx = WIDTH - 238
    _draw_panel(screen, rx, 8, 230, 72, BLUE)
    draw_text_left(screen, "Boy  (Arrows)", 15, BLUE, rx + 8, 12)
    _item_status(screen, rx + 10, 36, "Computer", 'computer' in boy.collected, _mini_computer)
    if boy_done:
        draw_text_left(screen, ">> Go to door!", 13, GREEN, rx + 10, 56)


def _item_status(screen, x, y, label, collected, icon_fn):
    icon_fn(screen, x, y)
    col = GREEN if collected else (140, 140, 140)
    mark = "  OK" if collected else ""
    draw_text_left(screen, f"{label}{mark}", 13, col, x + 22, y + 1)


# ── Mini icons ────────────────────────────────────────────────────

def _mini_canvas(surf, x, y):
    pygame.draw.rect(surf, DKBROWN, (x, y, 16, 13))
    pygame.draw.rect(surf, WHITE, (x + 2, y + 2, 12, 9))
    pygame.draw.circle(surf, RED, (x + 5, y + 5), 2)
    pygame.draw.circle(surf, BLUE, (x + 10, y + 7), 2)

def _mini_brush(surf, x, y):
    pygame.draw.rect(surf, DKBROWN, (x + 5, y, 4, 8))
    pygame.draw.rect(surf, ORANGE, (x + 3, y + 8, 8, 5), border_radius=1)
    pygame.draw.rect(surf, GREY, (x + 4, y + 6, 6, 3))

def _mini_computer(surf, x, y):
    pygame.draw.rect(surf, DKGREY, (x, y, 16, 11), border_radius=1)
    pygame.draw.rect(surf, CYAN, (x + 2, y + 2, 12, 7))
    pygame.draw.rect(surf, GREY, (x + 5, y + 11, 6, 2))
    pygame.draw.rect(surf, GREY, (x + 3, y + 13, 10, 1))


# ── Bottom bar ────────────────────────────────────────────────────

def draw_bottom_bar(screen):
    bar = pygame.Surface((WIDTH, 34), pygame.SRCALPHA)
    bar.fill((0, 0, 0, 190))
    screen.blit(bar, (0, HEIGHT - 34))
    draw_text(screen, "R  =  Restart Level", 16, WHITE, WIDTH // 2 - 120, HEIGHT - 19)
    draw_text(screen, "|", 16, GREY, WIDTH // 2, HEIGHT - 19)
    draw_text(screen, "ESC  =  Menu", 16, WHITE, WIDTH // 2 + 110, HEIGHT - 19)
