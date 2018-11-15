import pygame
from pygame.sprite import Sprite
from spritesheet import SpriteSheet


class FloatBlock(Sprite):

    def __init__(self, x, y, width, height, sheetx, sheety, scale):
        super(FloatBlock, self).__init__()
        self.scale = scale
        self.spritesheet = SpriteSheet('images/blocks.png')
        self.image = self.spritesheet.get_image(sheetx, sheety, width, height)
        self.image.set_colorkey((255, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*self.scale,
                                            self.image.get_height()*self.scale))
        self.rect = self.image.get_rect()
        self.rect.x = x*self.scale
        self.rect.y = y*self.scale
        self.origY = self.rect.y

        self.maxHeight = self.rect.y - (8*self.scale)
        self.last = pygame.time.get_ticks()

    def update(self):
        # Return to original position
        if self.rect.y < self.origY:
            self.rect.y += 2*self.scale





