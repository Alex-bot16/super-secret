"""
Level-building helpers.

Use these to build new levels quickly:
    plat(x, y, w)           → Platform
    moving(x, y, w, ...)    → MovingPlatform
    floor_at(y, x, w)       → floor Platform
    spikes_on(plat, side)   → Hazard on one edge, leaving safe space
    spikes_between(x, y, w) → freestanding spike strip
    water(x, w)             → deadly water at bottom
    lava_floor(x, w)        → deadly lava at bottom
    item(x, y, kind)        → Collectible
    door_pair(x, y)         → [girl Door, boy Door]
    level_dict(...)         → final level dictionary
"""
from constants import WIDTH, HEIGHT, TILE, SPIKE_HEIGHT, STONE
from objects import Platform, MovingPlatform, Hazard, Collectible, Door


def plat(x, y, w, colour=STONE, h=TILE):
    return Platform(x, y, w, h, colour)

def moving(x, y, w, colour, axis='x', dist=60, speed=0.03):
    return MovingPlatform(x, y, w, TILE, colour, axis, dist, speed)

def floor_at(y=HEIGHT - TILE, x=0, w=WIDTH, colour=STONE):
    return Platform(x, y, w, TILE, colour)

def spikes_on(platform, side='right', spike_width=40):
    """Spikes on one side of *platform*; always leaves ≥40 px safe."""
    px, py, pw = platform.rect.x, platform.rect.y, platform.rect.w
    spike_width = min(spike_width, pw - 40)
    if spike_width <= 0:
        spike_width = 16
    sx = px if side == 'left' else px + pw - spike_width
    return Hazard(sx, py - SPIKE_HEIGHT, spike_width, SPIKE_HEIGHT, 'spikes')

def spikes_between(x, y, w):
    return Hazard(x, y - SPIKE_HEIGHT, w, SPIKE_HEIGHT, 'spikes')

def water(x=0, w=WIDTH):
    return Hazard(x, HEIGHT - TILE, w, TILE, 'water_danger')

def lava_floor(x=0, w=WIDTH):
    return Hazard(x, HEIGHT - TILE, w, TILE, 'lava')

def item(x, y, kind):
    return Collectible(x, y, kind)

def door_pair(x, y, gap=60):
    return [Door(x, y, 'girl'), Door(x + gap, y, 'boy')]

def level_dict(theme, title, gx, gy, bx, by,
               platforms, hazards, collectibles, doors):
    return {
        'theme': theme, 'title': title,
        'girl_start': (gx, gy), 'boy_start': (bx, by),
        'platforms': platforms, 'hazards': hazards,
        'collectibles': collectibles, 'doors': doors,
    }
