# Mario player class

import pygame
from settings import Settings
from pygame.sprite import Sprite

class Mario(Sprite):
    def __init__(self, screen, settings, level):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.width = 50
        self.height = 50
        self.x = settings.screen_width
        self.y = settings.screen_height
        self.pos = (((self.x / 2) - 400), (self.y - 120))
        img = pygame.image.load('images/Mario_Sprite.jpg')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

        self.level = level

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

    def update(self):
        super().update()
        if self.moveRight:
            self.settings.camera.x += 1

        self.blitMario()

    def blitMario(self):
        self.level.blit(self.image, self.rect)
