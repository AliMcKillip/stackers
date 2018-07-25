from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
#this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640,480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 800)
        while self.gaming:
            for event in pygame.event.get():
                    x = 0
                    while x < 8:
                        sense.set_pixel (x, 7, (0, 0, 255))
                        time.sleep(0.5)
                        sense.set_pixel (x, 7, (0, 0, 0))
                        x +=1
                        if x == 8:
                            x = 0

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
