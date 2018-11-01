import pygame
from pygame.sprite import Sprite

class blockRect(Sprite):

    def __init__(self, x, y, width, height, scale):
        super(blockRect, self).__init__()
        self.image = pygame.Surface((width*scale, height*scale))
        self.rect = self.image.get_rect()
        self.rect.x = x*scale
        self.rect.y = y*scale
        self.image.fill((0, 0, 0))
