import pygame
import random
import ndjson
from config import *
from status import *
from quickdraw import QuickDrawData


def drawImage(surface, path, x, y, scale):
    img = pygame.image.load(path)
    img = pygame.transform.smoothscale(img, scale)
    surface.blit(img,(x - img.get_rect().size[0] // 2, y - img.get_rect().size[1] // 2))


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def drawText(surface, text, x, y, font, size, color):
    myFont = pygame.font.SysFont(font, size, True)
    textSurf, textRect = text_objects(text, myFont, color)
    textRect.center = (x, y)
    surface.blit(textSurf, textRect)

def drawDoodle(gameDisplay, tag, scale, pos):
    if tag not in Status.cache:
        return

    x, y = pos
    oscillate = 5
    surface = pygame.Surface((256, 256), pygame.SRCALPHA, 32)
    surface = surface.convert_alpha()

    for stroke in Status.cache[tag]:
        thisX = None
        thisY = None
        nextX = None
        nextY = None

        for i in range(len(stroke)-1):
            thisX = nextX if thisX else stroke[i][0] + random.random() * oscillate
            thisY = nextY if thisY else stroke[i][1] + random.random() * oscillate

            nextX = stroke[i+1][0] + random.random() * oscillate
            nextY = stroke[i+1][1] + random.random() * oscillate

            pygame.draw.line(surface, Config.white, (thisX, thisY), (nextX, nextY), 5)

    surface = pygame.transform.scale(surface, (int(256 * scale), int(256 * scale)))
    gameDisplay.blit(surface, (x, y))



def loadNdjson(tag, scale, pos, index=None, immutable=False):
    try:
        if tag not in Status.cache:
            qd = QuickDrawData(True)
            anvil = qd.get_drawing(tag, index)
            Status.cache[tag] = list(anvil.strokes)
            if not immutable:
                Status.objects[tag] = [scale, pos[0], pos[1]]
        if tag in Status.cache and not immutable:
            Status.objects[tag] = [scale, pos[0], pos[1]]
    except:
        pass

def conv(x, y):
    return (Status.offset + x, y)

def convR(x, y, w, h):
    return (Status.offset + x, y, w, h)