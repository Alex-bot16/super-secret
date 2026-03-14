"""
game.py – Main Game class: loop, state machine, gameplay logic.

Drawing is delegated to screens.py (menu/transitions) and hud.py (in-game UI).
"""
import pygame
import sys
import os

from constants import WIDTH, HEIGHT, FPS, PINK, BLUE, BLACK, WHITE
from utils import draw_text
from player import Player
from objects import MovingPlatform
from backgrounds import draw_level_bg
from levels import make_level
from hud import draw_hud, draw_bottom_bar
from screens import draw_menu, draw_level_complete, draw_game_complete


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Canvas & Code – A Cooperative Adventure")
        self.clock = pygame.time.Clock()

        # Music – put theme.mp3 next to main.py
        try:
            pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "theme.mp3"))
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        except pygame.error:
            pass

        self.girl = Player(60, 400,
            {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w},
            PINK, "Girl", "art")
        self.boy = Player(120, 400,
            {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP},
            BLUE, "Boy", "tech")

        self.state = 'menu'
        self.current_level = 1
        self.level_data = None
        self.transition_timer = 0
        self._menu_cd = 0

    # ── Level management ──────────────────────────────────────────

    def load_level(self, n):
        self.level_data = make_level(n)
        self.girl.reset(*self.level_data['girl_start'])
        self.boy.reset(*self.level_data['boy_start'])
        for c in self.level_data['collectibles']:
            c.collected = False
        self.state = 'playing'

    def _girl_done(self):
        return all(c.collected for c in self.level_data['collectibles']
                   if c.ctype in ('canvas', 'paintbrush'))

    def _boy_done(self):
        return all(c.collected for c in self.level_data['collectibles']
                   if c.ctype == 'computer')

    # ── Main loop ─────────────────────────────────────────────────

    def run(self):
        while True:
            self.clock.tick(FPS)
            if self._handle_events():
                return
            {'menu': self._tick_menu,
             'playing': self._tick_playing,
             'level_complete': self._tick_level_complete,
             'game_complete': self._tick_game_complete,
            }[self.state]()
            pygame.display.flip()

    def _handle_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); return True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                if self.state == 'playing':
                    self.state = 'menu'
                elif self.state == 'menu':
                    pygame.quit(); return True
        return False

    # ── Menu ──────────────────────────────────────────────────────

    def _tick_menu(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            self.load_level(self.current_level); return
        if self._menu_cd > 0:
            self._menu_cd -= 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.current_level = max(1, self.current_level - 1); self._menu_cd = 12
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.current_level = min(10, self.current_level + 1); self._menu_cd = 12
        draw_menu(self.screen, self.current_level, self.girl.controls, self.boy.controls)

    # ── Playing ───────────────────────────────────────────────────

    def _tick_playing(self):
        keys = pygame.key.get_pressed()
        d = self.level_data

        self.girl.handle_input(keys)
        self.boy.handle_input(keys)
        for p in d['platforms']:
            if isinstance(p, MovingPlatform):
                p.update()

        if (self.girl.update(d['platforms'], d['hazards']) == 'died' or
            self.boy.update(d['platforms'], d['hazards']) == 'died'):
            self.load_level(self.current_level); return

        for c in d['collectibles']:
            c.check_collect(self.girl)
            c.check_collect(self.boy)

        gd, bd = self._girl_done(), self._boy_done()
        for door in d['doors']:
            if door.for_player == 'girl': door.check_enter(self.girl, gd)
            else:                         door.check_enter(self.boy, bd)

        if self.girl.finished and self.boy.finished:
            self.state = 'game_complete' if self.current_level >= 10 else 'level_complete'
            self.transition_timer = 0

        if keys[pygame.K_r]:
            self.load_level(self.current_level); return

        self._draw_playing(gd, bd)

    def _draw_playing(self, gd, bd):
        d = self.level_data
        draw_level_bg(self.screen, self.current_level)
        for p in d['platforms']:    p.draw(self.screen)
        for h in d['hazards']:      h.draw(self.screen)
        for c in d['collectibles']: c.draw(self.screen)
        for door in d['doors']:     door.draw(self.screen, gd, bd)
        self.girl.draw(self.screen)
        self.boy.draw(self.screen)
        draw_hud(self.screen, self.girl, self.boy, gd, bd)
        # Title drawn AFTER hud so it doesn't bleed through transparent panels
        draw_text(self.screen, f"Level {self.current_level}: {d['title']}", 18, WHITE, WIDTH // 2, 92)
        draw_bottom_bar(self.screen)

    # ── Transitions ───────────────────────────────────────────────

    def _tick_level_complete(self):
        self.transition_timer += 1
        draw_level_complete(self.screen, self.current_level,
                            self.level_data['title'], self.transition_timer)
        if self.transition_timer > 60:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
                self.current_level += 1
                self.load_level(self.current_level)

    def _tick_game_complete(self):
        draw_game_complete(self.screen)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE]:
            self.current_level = 1
            self.state = 'menu'
