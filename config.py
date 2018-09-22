import pygame


class Config(object):
    pygame.init()
    info = pygame.display.Info()
    display_width = info.current_w
    display_height = info.current_h

    white = (255,255,255)
    black = (0,0,0)
    grey = (214, 215, 216)
    darkGrey = (127, 129, 130)
    red = (255,0,0)
    blue = (0, 134, 179)
