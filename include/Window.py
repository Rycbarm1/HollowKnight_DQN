from enum import Enum, unique


class TRAIN_STATION:

    WIDTH  = 200
    HEIGHT = 400


@unique
class WINDOW_SIZE(Enum):

    S = (0,  0,  990, 540)
    M = (100, 100, 990, 540)
    L = (200, 200, 990, 540)


class Screen():
    def __init__(self, size = (0, 0, 0, 0)):
        self.LEFT    = size[0]
        self.TOP     = size[1]
        self.WIDTH   = size[2]
        self.HEIGHT  = size[3]


WINDOWS  = { level : Screen(level.value) for level in WINDOW_SIZE}
STATIONS = { level : Screen(level.value) for level in WINDOW_SIZE}

for level in WINDOW_SIZE:

    STATIONS[level].LEFT   = WINDOWS[level].LEFT + 10
    STATIONS[level].TOP    = WINDOWS[level].TOP  + 30
    STATIONS[level].WIDTH  = WINDOWS[level].WIDTH  - WINDOWS[level].LEFT - 20
    STATIONS[level].HEIGHT = WINDOWS[level].HEIGHT - WINDOWS[level].TOP  - 40

