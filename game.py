import sys
import math
import threading
import speech
from config import *
from status import *
from util import *


def game():
    gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
    clock = pygame.time.Clock()

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Status.isQuit = True
                intro = False
                sys.exit()

        gameDisplay.fill(Config.black)

        pygame.draw.arc(gameDisplay, Config.white, (-200, Config.display_height // 2 + 100, Config.display_width + 400, Config.display_height // 2), 0, math.pi, 3)

        if Status.entitiesBuffer:
            entity = Status.entitiesBuffer.popleft()
            tag = entity.name
            loadNdjson(tag.lower())

        for tag in Status.objects:
            drawDoodle(gameDisplay, tag, 0.8, 100, 100)

        pygame.display.update()
        clock.tick(60)

def processingSpeech():
    print("here")
    speech.main()

def main():
    pygame.init()
    thread = threading.Thread(target=processingSpeech, args=())
    thread.start()
    game()


if __name__ == '__main__':
    main()