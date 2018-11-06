# Koopa enemy class

import pygame
from spritesheet import SpriteSheet

class Koopa():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.sprite = SpriteSheet('images/spritesheet.png')
        self.sprite.get_image(144, 0, 30, 26)
        self.images = list()
        self.width = 50
        self.height = 50
        self.images.append(self.sprite.get_image(144, 0, 30, 26))
        self.images.append(self.sprite.get_image(174, 0, 30, 26))
        self.images.append(self.sprite.get_image(204, 0, 30, 26))
        self.images.append(self.sprite.get_image(234, 0 , 30, 26))
        for i in range(4):
            self.images[i] = pygame.transform.scale(self.images[i], (self.width, self.height))
        self.rect = self.images[0].get_rect()

    def blitKoopa(self):
        if pygame.time.get_ticks() % 200 <= 50:
            self.screen.blit(self.images[0], self.rect)
        #elif pygame.time.get_ticks() % 200 <= 100:
        else:
            self.screen.blit(self.images[1], self.rect)
        # Need to flip koopa if walking on otherside
        '''
        elif pygame.time.get_ticks() % 200 <= 150:
            self.screen.blit(self.images[0], self.rect)
        else:
            self.screen.blit(self.images[1], self.rect)
        '''
