from enum import Enum, unique

# DEBUG 等级#
@unique
class DEBUG_LEVEL(Enum):
    NORMAL   = 0    # 游戏必要信息，
    INFO     = 1    # debug 文字信息
    IMG      = 2    # debug 图片信息
    ADDRESS  = 3    # debug 读取内存地址，慎用，信息很多