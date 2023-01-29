import pygame
from sys import exit
from settings import *
from engine import Engine

# here start the program
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Falling Sand')
    clock = pygame.time.Clock()
    engine = Engine()

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill('black')
        engine.run(screen)
        pygame.display.update()
        clock.tick(fps)
