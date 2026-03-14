"""backgrounds/ – Per-level background painters.

Usage:  draw_level_bg(surf, level_number)
"""
from backgrounds.geneva import draw_level_1, draw_level_2, draw_level_3
from backgrounds.alella import draw_level_4, draw_level_5, draw_level_6
from backgrounds.standrews_coast import draw_level_7, draw_level_8
from backgrounds.standrews_town import draw_level_9, draw_level_10

_DRAWERS = {
    1: draw_level_1,    2: draw_level_2,    3: draw_level_3,
    4: draw_level_4,    5: draw_level_5,    6: draw_level_6,
    7: draw_level_7,    8: draw_level_8,
    9: draw_level_9,   10: draw_level_10,
}


def draw_level_bg(surf, level_num):
    """Draw the background for level *level_num*."""
    drawer = _DRAWERS.get(level_num)
    if drawer:
        drawer(surf)
    else:
        surf.fill((0, 0, 0))
