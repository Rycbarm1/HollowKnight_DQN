import ctypes

ADDRESS={
        "Knight" :       {
            "Hp"         : {"value" : ctypes.c_long(),  "base" : 0x019D89E8, "offset" : [0x48 , 0x88,  0x70,  0x118, 0x58,  0x190]},
            "Soul"       : {"value" : ctypes.c_long(),  "base" : 0x019D89E8, "offset" : [0x48 , 0x88,  0x70,  0x118, 0x58,  0x1cc]},
            "Location_X" : {"value" : ctypes.c_float(), "base" : 0x019D8A18, "offset" : [0x580, 0x228, 0x728, 0x180, 0x140, 0xc  ]},
            "Location_Y" : {"value" : ctypes.c_float(), "base" : 0x019D8A18, "offset" : [0x580, 0x228, 0x728, 0x180, 0x140, 0x10 ]},
        },
        "False Knight" : {
            "Hp"         : {"value" : ctypes.c_long(),  "base" : 0x019D8A18, "offset" : [0x10,  0x18,  0x28,  0x28,  0x38,  0x140]},
            "Hp_1"       : {"value" : ctypes.c_long(),  "base" : 0x019D8A18, "offset" : [0x10,  0x18,  0x28,  0x28,  0x158, 0x140]},
            "Location_X" : {"value" : ctypes.c_float(), "base" : 0x019D89F0, "offset" : [0x478, 0x10,  0xD8,  0x10,  0x78,  0xC  ]},
            "Location_Y" : {"value" : ctypes.c_float(), "base" : 0x019D89F0, "offset" : [0x478, 0x10,  0xD8,  0x10,  0x78,  0x10 ]},
        },
        "Hornet Protector" : {
            "Hp"         : {"value" : ctypes.c_long(),  "base" : 0x019D8A18, "offset" : [0x10,  0x18,  0x28,  0x28,  0x38,  0x140]},
            "Location_X" : {"value" : ctypes.c_float(), "base" : 0x019D89F0, "offset" : [0x478, 0x10,  0xD8,  0x10,  0x78,  0xC  ]},
            "Location_Y" : {"value" : ctypes.c_float(), "base" : 0x019D89F0, "offset" : [0x478, 0x10,  0xD8,  0x10,  0x78,  0x10 ]},
        },
        "Broken vessel" :{
            "Hp"         : {"value" : ctypes.c_long(),  "base" : 0x019D8A18, "offset" : [0x10,  0x18,  0x28,  0x28,  0x38,  0x140]},
            "Location_X" : {"value" : ctypes.c_float(), "base" : 0x00000000, "offset" : [0xBE0, 0xFC0, 0x238, 0x130, 0x28,  0x140]},
            "Location_Y" : {"value" : ctypes.c_float(), "base" : 0x00000000, "offset" : [0xBE0, 0xFC0, 0x238, 0x130, 0x28,  0x140]},
        }
}