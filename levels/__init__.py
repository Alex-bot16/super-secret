"""levels/ – All 10 level definitions, split by city."""
from levels.geneva import level_1, level_2, level_3
from levels.alella import level_4, level_5, level_6
from levels.standrews import level_7, level_8, level_9, level_10

_LEVELS = {
    1: level_1,   2: level_2,   3: level_3,
    4: level_4,   5: level_5,   6: level_6,
    7: level_7,   8: level_8,   9: level_9,
    10: level_10,
}


def make_level(n):
    """Return the level dict for level *n* (1–10)."""
    return _LEVELS.get(n, level_1)()
