# Mario player class

import pygame
from settings import Settings
from pygame.sprite import Sprite
from spritesheet import SpriteSheet

class Mario(Sprite):
    def __init__(self, screen, settings, level):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.level = level
        self.spritesheet = SpriteSheet('images/mario.png')
        self.smallimages = list()
        for x in range(14):
            self.smallimages.append(self.spritesheet.get_image(80+(x*17), 34, 16, 16))
            self.smallimages[x] = pygame.transform.scale(self.smallimages[x],
                                                         (self.smallimages[x].get_width()*self.settings.scale,
                                                         self.smallimages[x].get_height()*self.settings.scale))
        self.image = self.smallimages[0]
        self.rect = self.image.get_rect()

        # Set starting Y:
        self.rect.y = 550

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False

        # TEMPORARY: Flag to check if camera is moving
        self.cameraMove = False

    def update(self):
        super().update()
        if self.moveRight:
            self.rect.x += 8
        if self.cameraMove:
            self.settings.camera.x += 8
        self.rect.y -= self.settings.gravity

        self.blitMario()

    def blitMario(self):
        self.level.blit(self.image, self.rect)
