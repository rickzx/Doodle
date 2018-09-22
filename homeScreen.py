import sys
from config import *
from status import *
from util import *


def homeScreen():
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

        tag = "apple"

        if tag in Status.cache:
            drawDoodle(gameDisplay, tag, 0.5, 100, 100)
        else:
            loadNdjson(tag)
            drawDoodle(gameDisplay, tag, 0.5, 100, 100)


        pygame.display.update()
        clock.tick(30)

def main():
    pygame.init()
    homeScreen()


if __name__ == '__main__':
    main()

