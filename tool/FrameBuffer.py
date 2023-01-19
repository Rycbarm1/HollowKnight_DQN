import threading
import time
import collections
import cv2
import win32gui, win32ui, win32con
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from include.HollowKnight import STATION, WINDOW

class FrameBuffer(threading.Thread):
    def __init__(self, threadID, name, maxlen=5):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.buffer = collections.deque(maxlen=maxlen)
        self.lock = threading.Lock()

        self._stop_event = threading.Event()
        
        self.hwnd = win32gui.GetDesktopWindow()

        self.hwindc = win32gui.GetWindowDC(self.hwnd)
        self.srcdc = win32ui.CreateDCFromHandle(self.hwindc)
        self.memdc = self.srcdc.CreateCompatibleDC()
        self.bmp = win32ui.CreateBitmap()
        self.bmp.CreateCompatibleBitmap(self.srcdc, WINDOW.WIDTH, WINDOW.HEIGHT)


    def run(self):
        while not self.stopped():
            #start = time.time()
            self.get_frame()
            #end = time.time()

            #HK.Debug("time : {}".format(end-start), debug_level=HK.DEBUG_LEVEL_0)
            time.sleep(0.05)
        self.srcdc.DeleteDC()
        self.memdc.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.hwindc)
        win32gui.DeleteObject(self.bmp.GetHandle())

    def get_frame(self):
        self.lock.acquire(blocking=True)
        station = cv2.resize(cv2.cvtColor(self.grab_screen(), cv2.COLOR_RGBA2RGB),(STATION.WIDTH,STATION.HEIGHT))
        self.buffer.append(tf.convert_to_tensor(station))
        self.lock.release()

    def get_buffer(self):
        stations = []
        self.lock.acquire(blocking=True)
        for f in self.buffer:
            stations.append(f)
        self.lock.release()
        return stations

    def stop(self):
        self._stop_event.set()
  
    def stopped(self):
        return self._stop_event.is_set()

    def grab_screen(self):
        self.memdc.SelectObject(self.bmp)
        self.memdc.BitBlt((0, 0), (WINDOW.WIDTH, WINDOW.HEIGHT), self.srcdc, (WINDOW.LEFT, WINDOW.TOP), win32con.SRCCOPY)
        
        signedIntsArray = self.bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (WINDOW.HEIGHT,WINDOW.WIDTH,4)

        return img