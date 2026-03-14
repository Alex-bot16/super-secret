"""Door – the exit each player must reach after collecting their items."""
import pygame

from constants import PINK, BLUE, GREEN, DKGREEN, WHITE, GOLD
from utils import draw_text


class Door:
    """Turns green when the matching player has all items."""

    def __init__(self, x, y, for_player):
        """for_player: 'girl' or 'boy'"""
        self.x = x
        self.y = y
        self.for_player = for_player
        self.rect = pygame.Rect(x, y, 32, 48)

    def draw(self, surf, girl_done, boy_done):
        done = girl_done if self.for_player == 'girl' else boy_done
        if done:
            colour, border = GREEN, DKGREEN
        elif self.for_player == 'girl':
            colour, border = PINK, (200, 100, 150)
        else:
            colour, border = BLUE, (40, 70, 180)

        pygame.draw.rect(surf, colour, self.rect, border_radius=4)
        pygame.draw.rect(surf, border, self.rect, 3, border_radius=4)

        # Doorknob
        kx = self.x + (24 if self.for_player == 'girl' else 8)
        pygame.draw.circle(surf, GOLD, (kx, self.y + 26), 3)

        # Label
        label = "A" if self.for_player == 'girl' else "T"
        draw_text(surf, label, 12, WHITE, self.x + 16, self.y + 10)

    def check_enter(self, player, all_items_collected):
        """Return True if this player enters their door with all items."""
        if not all_items_collected:
            return False
        if self.for_player == 'girl' and player.collect_type != 'art':
            return False
        if self.for_player == 'boy' and player.collect_type != 'tech':
            return False
        if player.rect.colliderect(self.rect):
            player.finished = True
            return True
        return False
