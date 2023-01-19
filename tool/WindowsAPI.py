import numpy as np
import win32gui, win32ui, win32con, win32api

from time import time
import include.HollowKnight as HK

GAME_START   = "F1"
GAME_START_1 = "ESC"
GAME_STOP    = "ESC"
GAME_OVER    = "F10"


# get windows image of hollow knight
def grab_screen():

    hwnd = win32gui.GetDesktopWindow()
    hwindc = win32gui.GetWindowDC(hwnd)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, HK.STATION.WIDTH, HK.STATION.HEIGHT)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (HK.STATION.WIDTH, HK.STATION.HEIGHT), srcdc, (HK.STATION.LEFT, HK.STATION.TOP), win32con.SRCCOPY)

    bmp.SaveBitmapFile(memdc, 'screen.bmp')
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (HK.STATION.HEIGHT,HK.STATION.WIDTH,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    end = time()
    HK.Debug(info="debug in test_restart", img=img, debug_level=HK.DEBUG_LEVEL.IMG)

    return img
  

# check which key is pressed
def key_check():
    operations = []
    if win32api.GetAsyncKeyState(0x41):
        operations.append("A")
    if win32api.GetAsyncKeyState(0x43):
        operations.append("C")
    if win32api.GetAsyncKeyState(0x58):
        operations.append("X")
    if win32api.GetAsyncKeyState(0x5A):
        operations.append("Z")
    if win32api.GetAsyncKeyState(0x1B):
        operations.append("ESC")
    if win32api.GetAsyncKeyState(0x70):
        operations.append("F1")
    if win32api.GetAsyncKeyState(0x79):
        operations.append("F10")

    direction = []
    if win32api.GetAsyncKeyState(0x25):
        direction.append("Left")
    if win32api.GetAsyncKeyState(0x26):
        direction.append("Up")
    if win32api.GetAsyncKeyState(0x27):
        direction.append("Right")
    if win32api.GetAsyncKeyState(0x28):
        direction.append("Down")

    return operations, direction


# win32 presskey and releasekey, but it has lag, what we need is in SendKey.py
def PressKey( hexKeyCode):
    win32api.keybd_event(hexKeyCode, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)


def ReleaseKey( hexKeyCode):
    win32api.keybd_event(hexKeyCode, 0, win32con.KEYEVENTF_KEYUP, 0)
