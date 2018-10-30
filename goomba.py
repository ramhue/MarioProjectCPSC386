# Goomba enemy class

import pygame
from settings import Settings

class Goomba():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.width = 50
        self.height = 50
        self.x = settings.screen_width
        self.y = settings.screen_height
        self.pos1 = (self.x / 2, self.y - 25)
        self.pos2 = ((self.x / 2) + 100, self.y - 25)
        img = pygame.image.load('images/goomba.png')
        img = pygame.transform.scale(img, (self.height, self.width))
        self.rect = img.get_rect()
        self.image = img

    def blitGoomba(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.image, self.pos2)