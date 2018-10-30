# Goomba enemy class

import pygame
from settings import Settings

class Mario():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.width = 50
        self.height = 50
        self.x = settings.screen_width
        self.y = settings.screen_height
        self.pos = (((self.x / 2) - 400), (self.y - 25))
        img = pygame.image.load('images/Mario_Sprite.jpg')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitMario(self):
        self.screen.blit(self.image, self.pos)
