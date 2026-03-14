"""Collectible – floating items players pick up.

Types: 'canvas', 'paintbrush' → collected by Girl (art)
       'computer'             → collected by Boy  (tech)
"""
import pygame
import math
import random

from constants import (
    RED, BLUE, GREEN, YELLOW, ORANGE, CYAN,
    WHITE, GREY, DKGREY, DKBROWN,
)


class Collectible:
    def __init__(self, x, y, ctype):
        self.x = x
        self.y = y
        self.ctype = ctype
        self.rect = pygame.Rect(x - 12, y - 12, 24, 24)
        self.collected = False
        self._bob_phase = random.random() * 6.28

    # ── public ────────────────────────────────────────────────────

    def check_collect(self, player):
        """Try to collect this item.  Returns True if picked up."""
        if self.collected:
            return False
        if not player.rect.colliderect(self.rect):
            return False
        if self._player_matches(player):
            self.collected = True
            player.collected.append(self.ctype)
            return True
        return False

    def draw(self, surf):
        if self.collected:
            return
        t = pygame.time.get_ticks() / 500 + self._bob_phase
        by = int(math.sin(t) * 4)
        cx, cy = int(self.x), int(self.y) + by

        self._draw_glow(surf, cx, cy)
        drawer = {
            'canvas':     self._draw_canvas,
            'paintbrush': self._draw_paintbrush,
            'computer':   self._draw_computer,
        }.get(self.ctype)
        if drawer:
            drawer(surf, cx, cy)

    # ── private ───────────────────────────────────────────────────

    def _player_matches(self, player):
        if self.ctype in ('canvas', 'paintbrush'):
            return player.collect_type == 'art'
        return self.ctype == 'computer' and player.collect_type == 'tech'

    @staticmethod
    def _draw_glow(surf, cx, cy):
        glow = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 255, 200, 60), (20, 20), 18)
        surf.blit(glow, (cx - 20, cy - 20))

    @staticmethod
    def _draw_canvas(surf, cx, cy):
        pygame.draw.rect(surf, DKBROWN, (cx - 10, cy - 10, 20, 16))
        pygame.draw.rect(surf, WHITE, (cx - 8, cy - 8, 16, 12))
        pygame.draw.circle(surf, RED, (cx - 3, cy - 3), 2)
        pygame.draw.circle(surf, BLUE, (cx + 3, cy - 1), 2)
        pygame.draw.circle(surf, YELLOW, (cx, cy + 1), 2)

    @staticmethod
    def _draw_paintbrush(surf, cx, cy):
        pygame.draw.rect(surf, DKBROWN, (cx - 2, cy - 8, 4, 12))
        pygame.draw.rect(surf, ORANGE, (cx - 4, cy + 3, 8, 6), border_radius=2)
        pygame.draw.rect(surf, YELLOW, (cx - 3, cy + 5, 6, 3), border_radius=1)
        pygame.draw.rect(surf, GREY, (cx - 3, cy + 1, 6, 3))

    @staticmethod
    def _draw_computer(surf, cx, cy):
        pygame.draw.rect(surf, DKGREY, (cx - 10, cy - 10, 20, 14), border_radius=2)
        pygame.draw.rect(surf, CYAN, (cx - 8, cy - 8, 16, 10))
        pygame.draw.rect(surf, GREY, (cx - 3, cy + 4, 6, 3))
        pygame.draw.rect(surf, GREY, (cx - 6, cy + 6, 12, 2))
        pygame.draw.line(surf, GREEN, (cx - 6, cy - 6), (cx, cy - 6), 1)
        pygame.draw.line(surf, WHITE, (cx - 6, cy - 3), (cx + 4, cy - 3), 1)
        pygame.draw.line(surf, GREEN, (cx - 4, cy), (cx + 2, cy), 1)
