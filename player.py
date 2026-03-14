"""Player class – input, movement, collision, and drawing."""
import pygame
import math

from constants import (
    WIDTH, HEIGHT, GRAVITY, PLAYER_SPEED, JUMP_POWER,
    BLACK, PINK, RED, BLUE, DKGREY, DKBROWN, BROWN,
)


class Player:
    def __init__(self, x, y, controls, colour, name, collect_type):
        self.start_x = x
        self.start_y = y
        self.x = float(x)
        self.y = float(y)
        self.w = 28
        self.h = 36
        self.vx = 0.0
        self.vy = 0.0
        self.speed = PLAYER_SPEED
        self.jump_power = JUMP_POWER
        self.on_ground = False
        self.controls = controls
        self.colour = colour
        self.name = name
        self.collect_type = collect_type
        self.collected = []       # list of ctype strings picked up
        self.finished = False     # True once they've entered their door
        self.facing = 1           # 1 = right,  -1 = left
        self.walk_frame = 0.0

    # ── helpers ───────────────────────────────────────────────────────

    @property
    def rect(self):
        """Current bounding box (recomputed every call)."""
        return pygame.Rect(int(self.x), int(self.y), self.w, self.h)

    def reset(self, x, y):
        """Put the player back at spawn and clear progress."""
        self.x, self.y = float(x), float(y)
        self.vx = self.vy = 0.0
        self.on_ground = False
        self.collected = []
        self.finished = False

    # ── input ─────────────────────────────────────────────────────────

    def handle_input(self, keys):
        """Read the keyboard and set horizontal velocity / jump."""
        self.vx = 0
        if keys[self.controls['left']]:
            self.vx = -self.speed
            self.facing = -1
        if keys[self.controls['right']]:
            self.vx = self.speed
            self.facing = 1
        if keys[self.controls['jump']] and self.on_ground:
            self.vy = self.jump_power
            self.on_ground = False

    # ── physics ───────────────────────────────────────────────────────

    def update(self, platforms, hazards):
        """
        Move the player, resolve collisions, check hazards.
        Returns 'died' if the player should respawn, else None.
        """
        self._apply_gravity()
        self._move_x(platforms)
        self._move_y(platforms)
        self._clamp_to_screen()
        self._advance_walk_animation()

        if self._fell_off_screen():
            return 'died'
        if self._touching_hazard(hazards):
            return 'died'
        return None

    def _apply_gravity(self):
        self.vy += GRAVITY
        if self.vy > 14:
            self.vy = 14  # terminal velocity

    def _move_x(self, platforms):
        self.x += self.vx
        r = self.rect
        for p in platforms:
            if r.colliderect(p.rect):
                if self.vx > 0:
                    self.x = p.rect.left - self.w
                elif self.vx < 0:
                    self.x = p.rect.right
                r = self.rect

    def _move_y(self, platforms):
        self.y += self.vy
        r = self.rect
        self.on_ground = False
        for p in platforms:
            if r.colliderect(p.rect):
                if self.vy > 0:          # falling → land on top
                    self.y = p.rect.top - self.h
                    self.vy = 0
                    self.on_ground = True
                elif self.vy < 0:        # rising → bump head
                    self.y = p.rect.bottom
                    self.vy = 0
                r = self.rect

    def _clamp_to_screen(self):
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.w:
            self.x = WIDTH - self.w

    def _fell_off_screen(self):
        return self.y > HEIGHT + 100

    def _touching_hazard(self, hazards):
        r = self.rect
        return any(r.colliderect(h.rect) for h in hazards)

    def _advance_walk_animation(self):
        if abs(self.vx) > 0:
            self.walk_frame += 0.15
        else:
            self.walk_frame = 0

    # ── drawing ───────────────────────────────────────────────────────

    def draw(self, surf):
        """Draw the player sprite at its current position."""
        if self.name == "Girl":
            self._draw_girl(surf)
        else:
            self._draw_boy(surf)

    def _draw_girl(self, surf):
        x, y, w, h = int(self.x), int(self.y), self.w, self.h
        f = self.facing
        skin = (255, 220, 185)
        # Dress
        pygame.draw.rect(surf, PINK, (x + 4, y + 14, w - 8, h - 18))
        pygame.draw.polygon(surf, PINK, [
            (x + 2, y + h - 4), (x + w - 2, y + h - 4),
            (x + w - 6, y + 22), (x + 6, y + 22)])
        # Head
        pygame.draw.circle(surf, skin, (x + w // 2, y + 8), 10)
        # Hair
        pygame.draw.circle(surf, BROWN, (x + w // 2, y + 5), 10)
        pygame.draw.rect(surf, BROWN, (x + 3, y + 2, 22, 8))
        pygame.draw.rect(surf, BROWN, (x + 2, y + 4, 4, 14))
        pygame.draw.rect(surf, BROWN, (x + w - 6, y + 4, 4, 14))
        # Eyes
        ex = x + w // 2 + f * 3
        pygame.draw.circle(surf, BLACK, (ex - 3, y + 9), 2)
        pygame.draw.circle(surf, BLACK, (ex + 3, y + 9), 2)
        # Legs & shoes
        pygame.draw.rect(surf, skin, (x + 7, y + h - 6, 5, 6))
        pygame.draw.rect(surf, skin, (x + w - 12, y + h - 6, 5, 6))
        pygame.draw.rect(surf, RED, (x + 6, y + h - 2, 7, 3))
        pygame.draw.rect(surf, RED, (x + w - 13, y + h - 2, 7, 3))

    def _draw_boy(self, surf):
        x, y, w, h = int(self.x), int(self.y), self.w, self.h
        f = self.facing
        skin = (240, 210, 170)
        # Shirt
        pygame.draw.rect(surf, BLUE, (x + 5, y + 14, w - 10, 14))
        # Pants
        pygame.draw.rect(surf, DKGREY, (x + 5, y + 26, w - 10, h - 30))
        # Head
        pygame.draw.circle(surf, skin, (x + w // 2, y + 8), 10)
        # Hair
        pygame.draw.rect(surf, DKBROWN, (x + 4, y - 1, 20, 8), border_radius=3)
        # Eyes
        ex = x + w // 2 + f * 3
        pygame.draw.circle(surf, BLACK, (ex - 3, y + 9), 2)
        pygame.draw.circle(surf, BLACK, (ex + 3, y + 9), 2)
        # Legs & shoes
        pygame.draw.rect(surf, DKGREY, (x + 7, y + h - 6, 5, 6))
        pygame.draw.rect(surf, DKGREY, (x + w - 12, y + h - 6, 5, 6))
        pygame.draw.rect(surf, BLACK, (x + 6, y + h - 2, 7, 3))
        pygame.draw.rect(surf, BLACK, (x + w - 13, y + h - 2, 7, 3))
