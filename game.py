import sys
import math
import threading
import speech
from config import *
from status import *
from util import *


def game():
    gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
    canvas = pygame.Surface((Config.display_width * 5, Config.display_height), pygame.SRCALPHA, 32)

    clock = pygame.time.Clock()

    intro = True

    loadNdjson("clock", 0.3, conv(Config.display_width // 2, Config.display_height // 2), 174, True)
    loadNdjson("ear", 0.3, conv(Config.display_width // 2, Config.display_height // 2), 116, True)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Status.isQuit = True
                intro = False
                sys.exit()

        canvas.fill(Config.black)

        if Status.mode == "Loading" and Status.entitiesBuffer:
            while (Status.entitiesBuffer):
                entity = Status.entitiesBuffer.popleft()
                if entity == "left":
                    Status.move = -1
                elif entity == "right":
                    Status.move = 1
                elif entity == "forward" or entity == "forwards":
                    Status.move = -2
                elif entity == "backward" or entity == "backwards":
                    Status.move = 2
                else:
                    tag = entity.name
                    loadNdjson(tag.lower(), 0.8, conv(1000, 500))
            
            Status.mode = "Listen"

        if Status.move == -1:
            Status.offset += 20
            if abs(Status.offset) % Config.display_width == 0:
                Status.move = 0

        elif Status.move == 1:
            Status.offset -= 20
            if abs(Status.offset) % Config.display_width == 0:
                Status.move = 0

        elif Status.move == -2:
            Status.scale += 0.2

        elif Status.move == 2:
            Status.scale -= 0.2

        print(Status.offset, Status.scale)

        for tag in Status.objects:
            drawDoodle(canvas, tag, Status.objects[tag][0], (Status.objects[tag][1], Status.objects[tag][2]))

        canvas = pygame.transform.scale(canvas, (canvas.get_rect().size[0] * Status.scale, canvas.get_rect().size[1] * Status.scale))
        gameDisplay.blit(canvas, (Status.offset, 0))

        pygame.draw.arc(gameDisplay, Config.white, (-400, Config.display_height // 2 + 300, Config.display_width + 800, Config.display_height // 2), 0, math.pi, 3)
        
        if Status.mode == "Listen":
            drawDoodle(gameDisplay, "ear", 0.3, (Config.display_width // 2, Config.display_height // 2))

        elif Status.mode == "Loading":
            drawDoodle(gameDisplay, "clock", 0.3, (Config.display_width // 2, Config.display_height // 2))

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