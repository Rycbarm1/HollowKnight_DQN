import win32gui
import win32api
import win32con
import win32process
import ctypes
import time

from include.Address import ADDRESS
from include.HollowKnight import Debug, DEBUG_LEVEL

ctypes.windll.user32.WindowFromPoint.restype = ctypes.c_void_p

Psapi = ctypes.WinDLL('Psapi.dll')
Kernel32 = ctypes.WinDLL('kernel32.dll')
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

def EnumProcessModulesEx(hProcess):
    buf_count = 256
    while True:
        LIST_MODULES_ALL = 0x03
        buf = (ctypes.wintypes.HMODULE * buf_count)()
        buf_size = ctypes.sizeof(buf)
        needed = ctypes.wintypes.DWORD()
        if not Psapi.EnumProcessModulesEx(hProcess, ctypes.byref(buf), buf_size, ctypes.byref(needed), LIST_MODULES_ALL):
            raise OSError('EnumProcessModulesEx failed')
        if buf_size < needed.value:
            buf_count = needed.value // (buf_size // buf_count)
            continue
        count = needed.value // (buf_size // buf_count)
        return map(ctypes.wintypes.HMODULE, buf[:count])

class Hp_getter():
    def __init__(self, hwnd):

        pid = win32process.GetWindowThreadProcessId(hwnd)[1]
        Debug("find pid %s with window %s"%(pid, hwnd), debug_level=DEBUG_LEVEL.NORMAL)
        self.process_handle = win32api.OpenProcess(0x1F0FFF, False, pid)
        self.kernal32 = ctypes.windll.LoadLibrary(r"C:\\Windows\\System32\\kernel32.dll")

        self.hx = 0
        # get dll address
        hProcess = Kernel32.OpenProcess(
        PROCESS_QUERY_INFORMATION | PROCESS_VM_READ,
        False, pid)
        hModule  = EnumProcessModulesEx(hProcess)
        for i in hModule:
            temp = win32process.GetModuleFileNameEx(self.process_handle,i.value)
            if temp[-15:] == "UnityPlayer.dll":
                self.UnityPlayer = i.value
          # if temp[-18:] == "mono-2.0-bdwgc.dll":
          #   print("%#x   "%i.value,end="")
          #   print(temp)
          #   self.mono = i.value

    def ReadProcessMemory(self, address, offset, result, final = False):
        if not self.kernal32.ReadProcessMemory(int(self.process_handle), ctypes.c_void_p(address + offset), ctypes.byref(result), 4 if final else 8, None):
            Debug('address 0x{:<12x} + 0x{:<3x} = 0x{:<12x}  can not read'.format(address, offset, address + offset), debug_level=DEBUG_LEVEL.ADDRESS)
            result.value = 0
            return False
        if final:
            Debug('address 0x{:<12x} + 0x{:<3x} = 0x{:<12x}   =     {}   '.format(address, offset, address + offset, result.value), debug_level=DEBUG_LEVEL.ADDRESS)
        else:
            Debug('address 0x{:<12x} + 0x{:<3x} = 0x{:<12x} ----> 0x{:x} '.format(address, offset, address + offset, result.value), debug_level=DEBUG_LEVEL.ADDRESS)
        return True

    def get_data(self, locate = "knight", info = "Hp"):

        offset_address = ctypes.c_longlong()
        base_address   = ADDRESS[locate][info]["base"]  + self.UnityPlayer
        offset_list    = ADDRESS[locate][info]["offset"]
        data_addres    = ADDRESS[locate][info]["value"]

        self.ReadProcessMemory(base_address, 0, offset_address)

        for offset in offset_list[:-1]:
            if not self.ReadProcessMemory(offset_address.value, offset, offset_address):
                return round(data_addres.value, 2)
        self.ReadProcessMemory(offset_address.value, offset_list[-1], data_addres, final = True)

        return 0 if ("Hp" in info ) and (data_addres.value < 0 or data_addres.value > 2000) else round(data_addres.value, 2)