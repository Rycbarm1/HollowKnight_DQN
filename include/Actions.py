import time
from tool.SendKey import PressKey, ReleaseKey

# Move Key
MOVE_UP    = 0x57  # W
MOVE_DOWN  = 0x53  # S
MOVE_LEFT  = 0x41  # A
MOVE_RIGHT = 0x44  # D

# other Key
ATTACK   = 0x4A # J
JUMP     = 0x4B # K
FOCUS    = 0x55 # U
CAST     = 0x48 # H
DASH     = 0xA0 # L_SHIFT


class Move:

    def __init__(self):
        pass

    def Move_Left(self):
        ReleaseKey(MOVE_RIGHT)
        PressKey(MOVE_LEFT)
        time.sleep(0.01)

    def Move_Right(self):
        ReleaseKey(MOVE_LEFT)
        PressKey(MOVE_RIGHT)
        time.sleep(0.01)

    def Stop(self):
        ReleaseKey(MOVE_LEFT)
        ReleaseKey(MOVE_RIGHT)
        pass

class Act:

    def __init__(self):
        pass

    def Attack(self):
        PressKey(ATTACK)
        time.sleep(0.15)
        ReleaseKey(ATTACK)
        time.sleep(0.01)

    def Attack_Down(self):
        PressKey(MOVE_DOWN)
        PressKey(ATTACK)
        time.sleep(0.05)
        ReleaseKey(ATTACK)
        ReleaseKey(MOVE_DOWN)
        time.sleep(0.01)

    def Attack_Up(self):
        PressKey(MOVE_UP)
        PressKey(ATTACK)
        time.sleep(0.11)
        ReleaseKey(ATTACK)
        ReleaseKey(MOVE_UP)
        time.sleep(0.01)

    def Short_Jump(self):
        PressKey(JUMP)
        time.sleep(0.2) 
        ReleaseKey(JUMP)

    def Mid_Jump(self):
        PressKey(JUMP)
        time.sleep(0.4)
        ReleaseKey(JUMP)

    def Skill_Up(self):
        PressKey(MOVE_UP)
        PressKey(CAST)
        time.sleep(0.15)
        ReleaseKey(MOVE_UP)
        ReleaseKey(CAST)
        time.sleep(0.15)

    def Skill_Down(self):
        PressKey(MOVE_DOWN)
        PressKey(CAST)
        time.sleep(0.2)
        ReleaseKey(MOVE_DOWN)
        ReleaseKey(CAST)
        time.sleep(0.3)

    def Rush(self):
        PressKey(DASH)
        time.sleep(0.1)
        ReleaseKey(DASH)

    def Cure(self):
        PressKey(FOCUS)
        time.sleep(1.4)
        ReleaseKey(FOCUS)
        time.sleep(0.1)


Act_Action  = Act()
Move_Action = Move()

Act_Actions  = []
Move_Actions = []

for func in dir(Act_Action):     
    if func.startswith('__'):
        continue
    Act_Actions.append(func)

for func in dir(Move_Action):     
    if func.startswith('__'):
        continue
    Move_Actions.append(func)

