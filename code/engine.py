import pygame
from sand import Sand
from settings import *
from random import choice


class Engine:
    def __init__(self):
        self.sand = pygame.sprite.Group()

        # sand spawn rate
        self.cooldown = 1

    def get_input(self):
        if self.cooldown >= 1:
            mouse = pygame.mouse
            if mouse.get_pressed()[0]:
                pos = mouse.get_pos()
                x = (pos[0]//sand_size) * sand_size
                y = (pos[1] // sand_size) * sand_size
                self.sand.add(Sand((x, y)))
                self.cooldown = 0

        elif self.cooldown < 1:
            self.cooldown += 0.3

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.sand.empty()

    def gravity(self):
        for grain in self.sand:
            if grain.moving:
                if grain.rect.bottom < screen_height:
                    occupation = self.lower_occupation(grain)

                    if not occupation[1]:
                        grain.update()

                    else:
                        self.diagonal_fall(grain, occupation)
                else:
                    grain.rect.bottom = screen_height
                    grain.moving = False

    def lower_occupation(self, grain):
        occupation = [False, False, False]
        grainx = grain.rect.x
        grainy = grain.rect.y
        for grain1 in self.sand:
            if grain1.rect.y == grainy + sand_size:
                if grain1.rect.x == grainx - sand_size:
                    occupation[0] = True
                    continue

                elif grain1.rect.x == grainx + sand_size:
                    occupation[2] = True
                    continue

            if grain1.rect.x == grainx and grain1.rect.top == grain.rect.bottom:
                occupation[1] = True

        return occupation

    def diagonal_fall(self, grain, occupation):
        if all(occupation):
            grain.moving = False
            return

        if not (occupation[0] + occupation[2]):
            occupation[choice((0, 2))] = True

        if occupation[0]:
            grain.rect.topleft = (grain.rect.x + sand_size, grain.rect.y + sand_size)

        elif occupation[2]:
            grain.rect.topleft = (grain.rect.x - sand_size, grain.rect.y + sand_size)

    def run(self, screen):
        self.get_input()
        self.gravity()
        self.sand.draw(screen)
