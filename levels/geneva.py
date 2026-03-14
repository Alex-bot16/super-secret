"""Geneva levels (1-3)."""
from constants import HEIGHT, TILE as T, STONE
from levels.helpers import (
    plat, floor_at, water, spikes_on, item, door_pair, level_dict,
)


def level_1():
    """Tutorial – gentle staircase, no hazards."""
    p1 = floor_at()
    p2 = plat(220, HEIGHT - 120, 150)
    p3 = plat(420, HEIGHT - 220, 150)
    p4 = plat(620, HEIGHT - 300, 170)
    p5 = plat(840, HEIGHT - 220, 180)

    return level_dict(
        'geneva', 'Lake Shore',
        60, HEIGHT - T - 40, 120, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5],
        hazards=[],
        collectibles=[
            item(290, HEIGHT - 160, 'canvas'),
            item(490, HEIGHT - 260, 'paintbrush'),
            item(700, HEIGHT - 340, 'computer'),
        ],
        doors=door_pair(860, HEIGHT - 220 - 48),
    )


def level_2():
    """Jet d'Eau – water gaps, stepping stones."""
    p1 = floor_at(x=0, w=260)
    p2 = plat(340, HEIGHT - 110, 130)
    p3 = plat(530, HEIGHT - 200, 130)
    p4 = plat(340, HEIGHT - 300, 130)
    p5 = plat(160, HEIGHT - 380, 140)
    p6 = plat(400, HEIGHT - 420, 140)
    p7 = plat(620, HEIGHT - 340, 120)
    p8 = plat(800, HEIGHT - 260, 200)

    return level_dict(
        'geneva', "Jet d'Eau",
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8],
        hazards=[water(260, 540)],
        collectibles=[
            item(400, HEIGHT - 150, 'canvas'),
            item(230, HEIGHT - 420, 'paintbrush'),
            item(460, HEIGHT - 460, 'computer'),
        ],
        doors=door_pair(830, HEIGHT - 260 - 48, gap=70),
    )


def level_3():
    """UN Quarter – taller climb, stepping stones."""
    p1  = floor_at(x=0, w=200)
    p2  = plat(260, HEIGHT - 110, 110)
    p3  = plat(430, HEIGHT - 210, 110)
    p4  = plat(280, HEIGHT - 310, 110)
    p5  = plat(490, HEIGHT - 320, 140)
    p6  = plat(690, HEIGHT - 240, 110)
    p7  = plat(690, HEIGHT - 370, 110)
    p8  = plat(510, HEIGHT - 460, 130)
    p9  = plat(300, HEIGHT - 520, 110)
    p10 = plat(100, HEIGHT - 450, 120)
    p11 = plat(800, HEIGHT - 310, 200)

    return level_dict(
        'geneva', 'UN Quarter',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11],
        hazards=[water(200, 600), spikes_on(p4, 'left', 40)],
        collectibles=[
            item(330, HEIGHT - 350, 'canvas'),
            item(560, HEIGHT - 500, 'paintbrush'),
            item(730, HEIGHT - 410, 'computer'),
        ],
        doors=door_pair(840, HEIGHT - 310 - 48, gap=60),
    )
