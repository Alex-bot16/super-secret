"""
constants.py – All game-wide settings live here.
Change these to tweak the feel of the whole game.
"""
import pygame

# ── Window ────────────────────────────────────────────────────────────
WIDTH  = 1024
HEIGHT = 768
FPS    = 60
TILE   = 40          # grid size used when building levels

# ── Physics ───────────────────────────────────────────────────────────
GRAVITY      = 0.6
PLAYER_SPEED = 4.5
JUMP_POWER   = -14   # negative = upward velocity

# Derived constants (don't edit – computed from the values above)
MAX_JUMP_HEIGHT = int(JUMP_POWER ** 2 / (2 * GRAVITY))   # ≈ 163 px
MAX_AIR_FRAMES  = int(2 * abs(JUMP_POWER) / GRAVITY)     # ≈ 47 frames
MAX_JUMP_DIST   = int(MAX_AIR_FRAMES * PLAYER_SPEED)     # ≈ 210 px

# ── Spike / Hazard sizing ─────────────────────────────────────────────
SPIKE_HEIGHT = 20    # how tall spike hazards are

# ── Colours ───────────────────────────────────────────────────────────
# Basics
WHITE      = (255, 255, 255)
BLACK      = (0,   0,   0)
GREY       = (180, 180, 180)
DKGREY     = (60,  60,  60)

# Primary
RED        = (220, 60,  60)
BLUE       = (60,  100, 220)
GREEN      = (60,  200, 80)
DKGREEN    = (30,  120, 50)
YELLOW     = (240, 220, 60)
ORANGE     = (240, 160, 40)
CYAN       = (60,  200, 220)
PINK       = (240, 130, 180)
PURPLE     = (160, 80,  220)

# Browns
BROWN      = (140, 90,  50)
DKBROWN    = (90,  55,  30)

# Scenery
SAND       = (230, 210, 170)
LTBLUE     = (170, 210, 240)
SKYBLUE    = (135, 200, 250)
WATER      = (50,  120, 200)
LAKEBLUE   = (70,  140, 210)
STONE      = (160, 155, 145)
VINE       = (100, 160, 60)
TERRACOTTA = (200, 110, 70)
CREAM      = (255, 248, 230)
GOLD       = (255, 200, 50)
