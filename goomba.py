# Goomba enemy class

import pygame
from settings import Settings
from spritesheet import SpriteSheet

class Goomba():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.sprite = SpriteSheet('images/spritesheet.png')
        self.sprite.get_image(0, 0, 10, 10)
        self.images = list()
        self.width = 50
        self.height = 50
        self.images.append(self.sprite.get_image(0, 0, 16, 20))
        self.images.append(self.sprite.get_image(30, 0, 16, 20))
        self.images.append(self.sprite.get_image(60, 0, 16, 20))
        for i in range(3):
            self.images[i] = pygame.transform.scale(self.images[i], (self.width, self.height))
        self.rect = self.images[0].get_rect()
        self.rect.x, self.rect. y = 50 * self.settings.scale, 50 * self.settings.scale

    def blitGoomba(self):
        if pygame.time.get_ticks() % 200 <= 50:
            self.screen.blit(self.images[0], self.rect)
        #elif pygame.time.get_ticks() % 200 <= 100:
        else:
            self.screen.blit(self.images[1], self.rect)
        '''
        elif pygame.time.get_ticks() % 200 <= 150:
            self.screen.blit(self.images[0], self.rect)
        else:
            self.screen.blit(self.images[1], self.rect)
        '''
