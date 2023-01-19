import matplotlib.pyplot as plt

from numpy import ndarray

from include.Debug  import DEBUG_LEVEL
from include.Window import WINDOWS, STATIONS, WINDOW_SIZE
from include.Game   import *


GLB_WINDO_SIZE  = WINDOW_SIZE.L
GLB_GAME_LEVEL  = GAME_LEVEL.ATTUNED
GLB_DEBUG_LEVEL = DEBUG_LEVEL.IMG


# 游戏窗口尺寸，不可更改，涉及到对特殊像素点的定位 #
WINDOW  = WINDOWS[GLB_WINDO_SIZE]
STATION = STATIONS[GLB_WINDO_SIZE]


# 游戏等级设定 #
LOCATE_LEVEL_X = { level : LOCATE_LEVELS_X[GLB_WINDO_SIZE][level] for level in GAME_LEVEL }
LOCATE_LEVEL_Y = { level : LOCATE_LEVELS_Y[GLB_WINDO_SIZE][level] for level in GAME_LEVEL }

# 游戏初始位置定位 #

LOCATE_DIR_LEFT_X  = LOCATE_DIRS_LEFT_X[GLB_WINDO_SIZE]
LOCATE_DIR_LEFT_Y  = LOCATE_DIRS_LEFT_Y[GLB_WINDO_SIZE]
LOCATE_DIR_RIGHT_X = LOCATE_DIRS_RIGHT_X[GLB_WINDO_SIZE]
LOCATE_DIR_RIGHT_Y = LOCATE_DIRS_RIGHT_Y[GLB_WINDO_SIZE]

# 关键信息debug #
def Debug(info = None, img = None, end = "\n", debug_level = DEBUG_LEVEL.NORMAL):

    if info:
        if debug_level is DEBUG_LEVEL.ADDRESS and GLB_DEBUG_LEVEL is DEBUG_LEVEL.ADDRESS:
            print(info, end=end)
            return True

        if ((debug_level is DEBUG_LEVEL.NORMAL) or (debug_level is DEBUG_LEVEL.INFO and GLB_DEBUG_LEVEL.value >= DEBUG_LEVEL.INFO.value)):
            print(info, end=end)

    if ndarray == type(img) and debug_level is DEBUG_LEVEL.IMG and GLB_DEBUG_LEVEL is debug_level:

        plt.imshow(img)
        plt.show()