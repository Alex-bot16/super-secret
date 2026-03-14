"""
utils.py – Small shared helpers used across the project.
"""
import pygame


def draw_text(surf, text, size, colour, cx, cy, font_name=None):
    """Draw *text* centred at *(cx, cy)*."""
    font = pygame.font.SysFont(font_name or "arial", size, bold=True)
    ts = font.render(text, True, colour)
    r = ts.get_rect(center=(cx, cy))
    surf.blit(ts, r)
    return r


def draw_text_left(surf, text, size, colour, x, y, font_name=None):
    """Draw *text* left-aligned with top-left at *(x, y)*."""
    font = pygame.font.SysFont(font_name or "arial", size, bold=True)
    ts = font.render(text, True, colour)
    surf.blit(ts, (x, y))
