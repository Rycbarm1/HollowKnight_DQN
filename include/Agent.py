
from include.Window import TRAIN_STATION
from include.Actions import Act_Actions, Move_Actions


# 训练参数 #
ACT_DIM    = len(Act_Actions)
MOVE_DIM   = len(Move_Actions)
FRAMEBUFFERSIZE = 4

INPUT_SHAPE = (FRAMEBUFFERSIZE, TRAIN_STATION.HEIGHT, TRAIN_STATION.WIDTH, 3)

GAMMA = 0
BATCH_SIZE         = 10  # 每次给agent learn的数据数量，从replay memory随机里sample一批数据出来
MEMORY_SIZE        = 200 # replay memory的大小，越大越占用内存
MEMORY_WARMUP_SIZE = 24  # replay_memory 里需要预存一些经验数据，再从里面sample一个batch的经验让agent去learn
LEARNING_RATE      = 0.00001  # 学习率