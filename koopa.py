# Koopa enemy class

import pygame
from spritesheet import SpriteSheet

class Koopa():
    def __init__(self, screen, settings, x, y):
        self.screen = screen
        self.settings = settings
        self.sprite = SpriteSheet('images/spritesheet.png')
        self.sprite.get_image(144, 0, 30, 26)
        self.images = list()
        self.width = 75
        self.height = 75
        self.animIter = 0
        self.last = pygame.time.get_ticks()
        self.images.append(self.sprite.get_image(144, 0, 30, 26))
        self.images.append(self.sprite.get_image(174, 0, 30, 26))
        self.images.append(self.sprite.get_image(204, 0, 30, 26))
        self.images.append(self.sprite.get_image(234, 0, 30, 26))
        for i in range(4):
            self.images[i] = pygame.transform.scale(self.images[i], (self.width, self.height))
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()
        self.rect.x, self.rect.y = x * self.settings.scale, y * self.settings.scale

    def blitKoopa(self):
        if pygame.time.get_ticks() > self.last + 500:
            if self.animIter == 1:
                self.animIter = 0
            else:
                self.animIter += 1
            self.image = self.images[self.animIter]
            self.last = pygame.time.get_ticks()

        self.screen.blit(self.image, self.rect)
