"""Platform and MovingPlatform – solid surfaces the player can stand on."""
import pygame
import math
import random

from constants import TILE, STONE


class Platform:
    """A solid, rectangular, static platform."""

    def __init__(self, x, y, w, h, colour=STONE):
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = colour

    def draw(self, surf):
        pygame.draw.rect(surf, self.colour, self.rect)
        darker = tuple(max(0, c - 30) for c in self.colour)
        pygame.draw.rect(surf, darker, self.rect, 2)


class MovingPlatform(Platform):
    """A platform that oscillates along one axis.

    Parameters
    ----------
    move_axis  : 'x' or 'y'
    move_range : pixels to oscillate each way
    speed      : radians per frame (0.02 = slow, 0.05 = fast)
    """

    def __init__(self, x, y, w, h, colour, move_axis, move_range, speed):
        super().__init__(x, y, w, h, colour)
        self.start_x = x
        self.start_y = y
        self.move_axis = move_axis
        self.move_range = move_range
        self.speed = speed
        self.t = random.random() * 6.28

    def update(self):
        self.t += self.speed
        if self.move_axis == 'x':
            self.rect.x = self.start_x + int(math.sin(self.t) * self.move_range)
        else:
            self.rect.y = self.start_y + int(math.sin(self.t) * self.move_range)
