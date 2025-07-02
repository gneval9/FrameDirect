# Made and developed by gneval9 Software
# 01-07-2025

import mmap
import os
import struct
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pygame.pkgdata')

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


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


def init_FD():
    global fb, fb_mem, screen_width, screen_height, bits_per_pixel
    fb = os.open("/dev/fb0", os.O_RDWR)

    pygame.init()
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    pygame.quit()

    #print("Resolucion: ", screen_width, "x", screen_height)

    bits_per_pixel = 32

    fb_mem = mmap.mmap(fb, screen_width * screen_height * (bits_per_pixel // 8),
                       mmap.MAP_SHARED, mmap.PROT_WRITE | mmap.PROT_READ, offset=0)


def draw_pixel(x, y, color):
    if fb_mem is None:
        raise RuntimeError("init_FD() no ha sido llamada o framebuffer cerrado.")
    offset = (y * screen_width + x) * 4
    fb_mem.seek(offset)
    fb_mem.write(struct.pack('I', color))


def close():
    global fb, fb_mem
    if fb_mem is not None:
        fb_mem.close()
        fb_mem = None
    if fb is not None:
        os.close(fb)
        fb = None