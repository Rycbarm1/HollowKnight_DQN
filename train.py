# -*- coding: utf-8 -*-
import time
import tensorflow as tf
import win32gui, win32con

from include.Agent import *
from include.HollowKnight import WINDOW, DEBUG_LEVEL, Debug

from core1.DQN   import DQN
from core1.Agent import Agent
from core1.Model import Model
from core1.ReplayMemory import ReplayMemory

from tool.Actions import restart
from tool.GetHP   import Hp_getter
from tool.Helper  import pause_game


def locate_game():

    while True:
        hwnd = win32gui.FindWindow(None, "Hollow Knight")
        if 0 == hwnd:
            print("can not find window with Hollow Knight ")
            time.sleep(1)
            continue
        print("find window %s with Hollow Knight"%hwnd)
        break
    win32gui.ShowWindow(hwnd,win32con.SW_SHOWNORMAL)
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, WINDOW.LEFT, WINDOW.TOP, WINDOW.WIDTH, WINDOW.HEIGHT, win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(hwnd)

    return hwnd


def run_episode(hp, algorithm,agent,act_rmp_correct, move_rmp_correct,PASS_COUNT,paused):
    restart()


if __name__ == '__main__':
    # In case of out of memory
    config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True      #程序按需申请内存
    sess = tf.compat.v1.Session(config = config)

    total_reward = 0
    total_remind_hp = 0

    act_rmp_correct = ReplayMemory(MEMORY_SIZE, file_name='./mode/memory/act')         # experience pool
    move_rmp_correct = ReplayMemory(MEMORY_SIZE,file_name='./mode/memory/move')         # experience pool
    
    # new model, if exit save file, load it
    hwnd= locate_game()

    # Hp counter
    hp    = Hp_getter(hwnd)
    model = Model(INPUT_SHAPE, ACT_DIM, MOVE_DIM)

    algorithm = DQN(model, gamma=GAMMA, learnging_rate=LEARNING_RATE)
    agent = Agent(ACT_DIM, algorithm, e_greed=0.12, e_greed_decrement=1e-6)

    # paused at the begining
    paused = True
    paused = pause_game(paused)
    Debug("start train", debug_level=DEBUG_LEVEL.NORMAL)

    # 开始训练
    max_episode = 30000
    episode     = 0
    PASS_COUNT  = 0                 # pass count

    while episode < max_episode:    # 训练max_episode个回合，test部分不计算入episode数量
        # 训练
        episode += 1
        reward, total_step, PASS_COUNT, remind_hp = run_episode(hp, algorithm,agent,act_rmp_correct, move_rmp_correct, PASS_COUNT, paused)
        with open("history.txt", "a") as file:
            file.writelines("Episode: {}, pass_count: {}, hp: {}, this time reward : {}, ave reward : {}\n\n".format(episode, PASS_COUNT, total_remind_hp / episode, reward, total_reward/episode))
            Debug("Episode: {}, pass_count: {}, hp: {}, this time reward : {}, ave reward : {}".format(episode, PASS_COUNT, total_remind_hp / episode, reward, total_reward/episode), debug_level=DEBUG_LEVEL.NORMAL)
