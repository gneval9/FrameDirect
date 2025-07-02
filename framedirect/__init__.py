# Made and developed by gneval9 Software
# 01-07-2025

import mmap
import os
import struct
import warnings


RED     = 0xFFFF0000
GREEN   = 0xFF00FF00
BLUE    = 0xFF0000FF
WHITE   = 0xFFFFFFFF
BLACK   = 0xFF000000
YELLOW  = 0xFFFFFF00
CYAN    = 0xFF00FFFF
MAGENTA = 0xFFFF00FF
GRAY    = 0xFF888888
ORANGE  = 0xFFFFA500


fb = None
fb_mem = None
screen_width = 0
screen_height = 0
bits_per_pixel = 32


def init():
    global fb, fb_mem, screen_width, screen_height, bits_per_pixel
    fb = os.open("/dev/fb0", os.O_RDWR)

    try:
        with open("/sys/class/graphics/fb0/virtual_size", "r") as f:
            res = f.read().strip()
            screen_width, screen_height = map(int, res.split(","))
    except Exception as e:
        raise RuntimeError(f"No se pudo obtener la resolución del framebuffer: {e}")


    bits_per_pixel = 32

    fb_mem = mmap.mmap(fb, screen_width * screen_height * (bits_per_pixel // 8),
                       mmap.MAP_SHARED, mmap.PROT_WRITE | mmap.PROT_READ, offset=0)


def draw_pixel(x, y, color):
    if fb_mem is None:
        raise RuntimeError("init() no ha sido llamada o framebuffer cerrado.")
    offset = (y * screen_width + x) * 4
    fb_mem.seek(offset)
    fb_mem.write(struct.pack('I', color))

def resolution():
        print("Resolucion: ", screen_width, "x", screen_height)

def close():
    global fb, fb_mem
    if fb_mem is not None:
        fb_mem.close()
        fb_mem = None
    if fb is not None:
        os.close(fb)
        fb = None
