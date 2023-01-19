from enum import Enum, unique
from include.Window import WINDOW_SIZE

# 游戏等级设定 #
@unique
class GAME_LEVEL(Enum):
    ATTUNED  = 0    # 调谐
    ASCENDED = 1    # 进升 
    REDIANT  = 2    # 幅辉

LOCATE_LEVELS_X = {}
LOCATE_LEVELS_Y = {}
LOCATE_LEVELS_X[WINDOW_SIZE.S] = {GAME_LEVEL.ATTUNED  : 565,
                                  GAME_LEVEL.ASCENDED : 565,
                                  GAME_LEVEL.REDIANT  : 565,}

LOCATE_LEVELS_X[WINDOW_SIZE.M] = {GAME_LEVEL.ATTUNED  : 565,
                                  GAME_LEVEL.ASCENDED : 565,
                                  GAME_LEVEL.REDIANT  : 565,}


LOCATE_LEVELS_X[WINDOW_SIZE.L] = {GAME_LEVEL.ATTUNED  : 565,
                                  GAME_LEVEL.ASCENDED : 565,
                                  GAME_LEVEL.REDIANT  : 565,}


LOCATE_LEVELS_Y[WINDOW_SIZE.S] = {GAME_LEVEL.ATTUNED  : 259,
                                  GAME_LEVEL.ASCENDED : 311,
                                  GAME_LEVEL.REDIANT  : 363,}

LOCATE_LEVELS_Y[WINDOW_SIZE.M] = {GAME_LEVEL.ATTUNED  : 259,
                                  GAME_LEVEL.ASCENDED : 311,
                                  GAME_LEVEL.REDIANT  : 363,}


LOCATE_LEVELS_Y[WINDOW_SIZE.L] = {GAME_LEVEL.ATTUNED  : 259,
                                  GAME_LEVEL.ASCENDED : 311,
                                  GAME_LEVEL.REDIANT  : 363,}
                        

LOCATE_DIRS_LEFT_X  = {}
LOCATE_DIRS_RIGHT_Y = {}
LOCATE_DIRS_RIGHT_X = {}

LOCATE_DIRS_RIGHT_Y[WINDOW_SIZE.S] = 425
LOCATE_DIRS_RIGHT_Y[WINDOW_SIZE.M] = 425
LOCATE_DIRS_RIGHT_Y[WINDOW_SIZE.L] = 425
LOCATE_DIRS_LEFT_Y = LOCATE_DIRS_RIGHT_Y

LOCATE_DIRS_LEFT_X[WINDOW_SIZE.S]  = 518
LOCATE_DIRS_LEFT_X[WINDOW_SIZE.M]  = 518
LOCATE_DIRS_LEFT_X[WINDOW_SIZE.L]  = 518

LOCATE_DIRS_RIGHT_X[WINDOW_SIZE.S] = 460
LOCATE_DIRS_RIGHT_X[WINDOW_SIZE.M] = 460
LOCATE_DIRS_RIGHT_X[WINDOW_SIZE.L] = 460