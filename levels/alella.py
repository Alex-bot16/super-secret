"""Alella levels (4-6)."""
from constants import HEIGHT, TILE as T, TERRACOTTA, DKBROWN, VINE
from levels.helpers import (
    plat, floor_at, lava_floor, spikes_on, spikes_between,
    item, door_pair, level_dict,
)


def level_4():
    """Village Square – floor with platforms, ground spikes."""
    p1 = floor_at()
    p2 = plat(200, HEIGHT - 120, 130, TERRACOTTA)
    p3 = plat(400, HEIGHT - 210, 120, TERRACOTTA)
    p4 = plat(580, HEIGHT - 130, 110, TERRACOTTA)
    p5 = plat(720, HEIGHT - 240, 140, TERRACOTTA)
    p6 = plat(890, HEIGHT - 160, 130, TERRACOTTA)

    return level_dict(
        'alella', 'Village Square',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6],
        hazards=[],
        collectibles=[
            item(260, HEIGHT - 160, 'canvas'),
            item(460, HEIGHT - 250, 'paintbrush'),
            item(790, HEIGHT - 280, 'computer'),
        ],
        doors=door_pair(900, HEIGHT - 160 - 48),
    )


def level_5():
    """Vineyards – descending path, lava at bottom."""
    p1 = plat(0, 240, 200, TERRACOTTA)
    p2 = plat(260, 300, 150, VINE)
    p3 = plat(470, 240, 130, VINE)
    p4 = plat(650, 330, 140, TERRACOTTA)
    p5 = plat(450, 430, 130, VINE)
    p6 = plat(230, 500, 140, TERRACOTTA)
    p7 = plat(470, 540, 140, VINE)
    p8 = plat(690, 470, 120, TERRACOTTA)
    p9 = plat(850, 560, 170, TERRACOTTA)

    return level_dict(
        'alella', 'Vineyards',
        40, 200, 100, 200,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9],
        hazards=[lava_floor()],
        collectibles=[
            item(330, 260, 'paintbrush'),
            item(710, 290, 'canvas'),
            item(730, 430, 'computer'),
        ],
        doors=door_pair(870, 560 - 48, gap=60),
    )


def level_6():
    """Bodega – climb with lava below."""
    p1  = floor_at(x=0, w=220, colour=TERRACOTTA)
    p2  = plat(300, HEIGHT - 120, 110, DKBROWN)
    p3  = plat(470, HEIGHT - 230, 110, DKBROWN)
    p4  = plat(300, HEIGHT - 330, 120, DKBROWN)
    p5  = plat(140, HEIGHT - 420, 110, TERRACOTTA)
    p6  = plat(350, HEIGHT - 490, 130, DKBROWN)
    p7  = plat(570, HEIGHT - 400, 110, TERRACOTTA)
    p8  = plat(570, HEIGHT - 530, 110, DKBROWN)
    p9  = plat(770, HEIGHT - 450, 110, TERRACOTTA)
    p10 = plat(860, HEIGHT - 200, 160, TERRACOTTA)
    p11 = floor_at(x=860, w=164, colour=TERRACOTTA)

    return level_dict(
        'alella', 'Bodega',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11],
        hazards=[lava_floor(220, 640)],
        collectibles=[
            item(180, HEIGHT - 460, 'canvas'),
            item(420, HEIGHT - 530, 'paintbrush'),
            item(610, HEIGHT - 570, 'computer'),
        ],
        doors=door_pair(880, HEIGHT - 200 - 48, gap=60),
    )
