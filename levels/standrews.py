"""St Andrews levels (7-10)."""
from constants import HEIGHT, TILE as T, STONE, DKGREEN
from levels.helpers import (
    plat, water, lava_floor, spikes_on, item, door_pair, level_dict,
)


def level_7():
    """The Pier – water below, stepping stones."""
    p1 = plat(0, HEIGHT - T, 180)
    p2 = plat(260, HEIGHT - 100, 120)
    p3 = plat(450, HEIGHT - 190, 120)
    p4 = plat(630, HEIGHT - 110, 120)
    p5 = plat(800, HEIGHT - 210, 110)
    p6 = plat(860, HEIGHT - 320, 160)

    return level_dict(
        'standrews', 'The Pier',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6],
        hazards=[water(180, 680)],
        collectibles=[
            item(320, HEIGHT - 140, 'canvas'),
            item(690, HEIGHT - 150, 'paintbrush'),
            item(850, HEIGHT - 250, 'computer'),
        ],
        doors=door_pair(880, HEIGHT - 320 - 48, gap=60),
    )


def level_8():
    """Castle Ruins – tall climb, water below."""
    p1  = plat(0, HEIGHT - T, 170)
    p2  = plat(230, HEIGHT - 120, 110)
    p3  = plat(410, HEIGHT - 230, 120)
    p4  = plat(250, HEIGHT - 340, 110)
    p5  = plat(470, HEIGHT - 360, 110)
    p6  = plat(350, HEIGHT - 460, 120)
    p7  = plat(570, HEIGHT - 480, 110)
    p8  = plat(730, HEIGHT - 390, 110)
    p9  = plat(730, HEIGHT - 530, 110)
    p10 = plat(890, HEIGHT - 460, 130)

    return level_dict(
        'standrews', 'Castle Ruins',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10],
        hazards=[
            water(170, 720),
            spikes_on(p3, 'right', 40),
        ],
        collectibles=[
            item(300, HEIGHT - 380, 'canvas'),
            item(410, HEIGHT - 500, 'paintbrush'),
            item(780, HEIGHT - 570, 'computer'),
        ],
        doors=door_pair(900, HEIGHT - 460 - 48),
    )


def level_9():
    """The Old Course – golf-green platforms, tricky gaps."""
    p1  = plat(0, HEIGHT - T, 160, DKGREEN)
    p2  = plat(230, HEIGHT - 110, 110, DKGREEN)
    p3  = plat(400, HEIGHT - 210, 100, DKGREEN)
    p4  = plat(550, HEIGHT - 310, 110, DKGREEN)
    p5  = plat(370, HEIGHT - 390, 110, DKGREEN)
    p6  = plat(170, HEIGHT - 470, 110, STONE)
    p7  = plat(390, HEIGHT - 530, 110, DKGREEN)
    p8  = plat(600, HEIGHT - 450, 100, DKGREEN)
    p9  = plat(740, HEIGHT - 550, 110, STONE)
    p10 = plat(860, HEIGHT - 450, 160, DKGREEN)

    return level_dict(
        'standrews', 'The Old Course',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10],
        hazards=[
            water(160, 700),
        ],
        collectibles=[
            item(280, HEIGHT - 150, 'canvas'),
            item(220, HEIGHT - 510, 'paintbrush'),
            item(790, HEIGHT - 590, 'computer'),
        ],
        doors=door_pair(880, HEIGHT - 450 - 48, gap=60),
    )


def level_10():
    """The Cathedral – final challenge, lava, spikes on edges."""
    p1  = plat(0, HEIGHT - T, 130)
    p2  = plat(200, HEIGHT - 110, 100)
    p3  = plat(360, HEIGHT - 220, 100)
    p4  = plat(210, HEIGHT - 320, 100)
    p5  = plat(420, HEIGHT - 340, 110)
    p6  = plat(290, HEIGHT - 440, 100)
    p7  = plat(140, HEIGHT - 530, 110)
    p8  = plat(350, HEIGHT - 550, 100)
    p9  = plat(540, HEIGHT - 470, 100)
    p10 = plat(680, HEIGHT - 390, 100)
    p11 = plat(680, HEIGHT - 530, 110)
    p12 = plat(840, HEIGHT - 450, 100)
    p13 = plat(880, HEIGHT - 200, 140)
    p14 = plat(880, HEIGHT - 570, 140)

    return level_dict(
        'standrews', 'The Cathedral',
        40, HEIGHT - T - 40, 100, HEIGHT - T - 40,
        platforms=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14],
        hazards=[
            lava_floor(130, 750),
            spikes_on(p3, 'right', 35),
            spikes_on(p5, 'right', 40),
            spikes_on(p10, 'right', 35),
        ],
        collectibles=[
            item(260, HEIGHT - 360, 'canvas'),
            item(190, HEIGHT - 570, 'paintbrush'),
            item(730, HEIGHT - 570, 'computer'),
        ],
        doors=door_pair(900, HEIGHT - 570 - 48),
    )
