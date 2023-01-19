import cv2
from include.Actions import *
from include.HollowKnight import *
from tool.WindowsAPI import grab_screen


def take_act(act):
    getattr(Act_Action, act)() 


def take_move(move):
    getattr(Move_Action, move)()


def Look_up():
    PressKey(MOVE_UP)
    time.sleep(0.1)
    ReleaseKey(MOVE_UP)


def Locate():
    PressKey(JUMP)
    time.sleep(0.1)
    ReleaseKey(JUMP)


def judge_face(station):

    Debug("debug in judge_station    ", end = "", debug_level=DEBUG_LEVEL.INFO)

    if (station[LOCATE_DIR_RIGHT_Y][LOCATE_DIR_RIGHT_X].tolist() == [255, 255,255] and
        station[LOCATE_DIR_RIGHT_Y][LOCATE_DIR_RIGHT_X + 5].tolist() != [255, 255,255] and
        station[LOCATE_DIR_RIGHT_Y][LOCATE_DIR_RIGHT_X + 10].tolist() == [255, 255,255]):
        
        Debug("face to right", debug_level=DEBUG_LEVEL.INFO)

        return True
    
    if (station[LOCATE_DIR_LEFT_Y][LOCATE_DIR_RIGHT_X].tolist() == [255, 255,255] and
        station[LOCATE_DIR_LEFT_Y][LOCATE_DIR_RIGHT_X + 5].tolist() != [255, 255,255] and
        station[LOCATE_DIR_LEFT_Y][LOCATE_DIR_RIGHT_X + 10].tolist() == [255, 255,255]):
        Debug("face to left", debug_level=DEBUG_LEVEL.INFO)
        return True

    Debug("face check issue", debug_level=DEBUG_LEVEL.INFO)

    return False


def judge_level(station):

    is_find = False

    for level in GAME_LEVEL:

        if station[LOCATE_LEVEL_Y[level]][LOCATE_LEVEL_X[level]].tolist() == [255, 255,255] and level == GLB_GAME_LEVEL :
            Debug("debug in judge_level    ", end = "", debug_level=DEBUG_LEVEL.INFO)
            return True

    return False


def restart():

    while True:
        Locate()
        time.sleep(0.7)
        station = cv2.resize(cv2.cvtColor(grab_screen(), cv2.COLOR_RGBA2RGB),(WINDOW.WIDTH,WINDOW.HEIGHT))

        Debug("debug in test_restart", debug_level=DEBUG_LEVEL.INFO)

        if judge_face(station): 
            Look_up()
            break

    time.sleep(1)
    while True:
        time.sleep(0.2)
        station = cv2.resize(cv2.cvtColor(grab_screen(), cv2.COLOR_RGBA2RGB),(WINDOW.WIDTH,WINDOW.HEIGHT))
        if judge_level(station): break
        Look_up()

    Locate()