import pygame
from settings import *
from random import randint


class Sand(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((sand_size, sand_size))
        # self.image.fill((randint(100, 200), randint(50, 100), randint(0, 50)))
        # self.image.fill((randint(50, 200), randint(50, 200), randint(50, 200)))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect(topleft=pos)

        self.moving = True

    def update(self):
        self.rect.y += gravity
