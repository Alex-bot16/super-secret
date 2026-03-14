"""Hazard – deadly zones that kill on contact (spikes, water, lava)."""
import pygame
import math

from constants import RED, ORANGE, YELLOW


class Hazard:
    """Types: 'spikes', 'water_danger', 'lava'."""

    def __init__(self, x, y, w, h, htype='spikes'):
        self.rect = pygame.Rect(x, y, w, h)
        self.htype = htype

    def draw(self, surf):
        if self.htype == 'spikes':
            self._draw_spikes(surf)
        elif self.htype == 'water_danger':
            self._draw_water(surf)
        elif self.htype == 'lava':
            self._draw_lava(surf)

    def _draw_spikes(self, surf):
        n = max(1, self.rect.w // 16)
        for i in range(n):
            bx = self.rect.x + i * 16
            pygame.draw.polygon(surf, RED, [
                (bx, self.rect.bottom),
                (bx + 8, self.rect.top),
                (bx + 16, self.rect.bottom),
            ])

    def _draw_water(self, surf):
        pygame.draw.rect(surf, (30, 60, 160), self.rect)
        t = pygame.time.get_ticks() / 300
        for i in range(0, self.rect.w, 20):
            wy = self.rect.y + int(math.sin(t + i * 0.3) * 3)
            pygame.draw.circle(surf, (60, 100, 200),
                               (self.rect.x + i + 10, wy), 6)

    def _draw_lava(self, surf):
        pygame.draw.rect(surf, ORANGE, self.rect)
        t = pygame.time.get_ticks() / 200
        for i in range(0, self.rect.w, 12):
            ly = self.rect.y + int(math.sin(t + i * 0.5) * 3)
            pygame.draw.circle(surf, YELLOW, (self.rect.x + i + 6, ly), 5)
