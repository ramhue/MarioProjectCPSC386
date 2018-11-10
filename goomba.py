# Goomba enemy class

import pygame
from settings import Settings
from spritesheet import SpriteSheet
from pygame.sprite import Group
from pygame.sprite import Sprite


class Goomba(Sprite):
    def __init__(self, screen, settings, x, y):
        super(Goomba, self).__init__()
        self.screen = screen
        self.settings = settings
        self.sprite = SpriteSheet('images/spritesheet.png')
        self.images = list()
        self.width = 50
        self.height = 50
        self.animIter = 0
        self.last = pygame.time.get_ticks()
        self.images.append(self.sprite.get_image(0, 0, 16, 20))
        self.images.append(self.sprite.get_image(30, 0, 16, 20))
        self.images.append(self.sprite.get_image(60, 0, 16, 20))

        for i in range(3):
            self.images[i] = pygame.transform.scale(self.images[i], (self.width, self.height))

        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.rect.x, self.rect.y = x * self.settings.scale, y * self.settings.scale

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        self.delta = 5
        self.u = 1

    def update(self):
        super().update()
        self.rect.x -= 1
        self.rect.y -= self.settings.gravity

    def blitGoomba(self):
        if pygame.time.get_ticks() > self.last + 500:
            if self.animIter == 1:
                self.animIter = 0
            else:
                self.animIter += 1
            self.image = self.images[self.animIter]
            self.last = pygame.time.get_ticks()

        self.screen.blit(self.image, self.rect)

