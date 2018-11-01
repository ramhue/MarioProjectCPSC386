# Mario player class

import pygame
from settings import Settings
from pygame.sprite import Sprite

class Mario(Sprite):
    def __init__(self, screen, settings, level):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.level = level
        self.width = 50
        self.height = 50
        self.x = settings.screen_width
        self.y = settings.screen_height
        self.image = pygame.image.load('images/Mario_Sprite.jpg')
        self.image = pygame.transform.scale(self.image, (self.height, self.width))
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
            self.rect.x += 1
        if self.cameraMove:
            self.settings.camera.x += 1

        self.blitMario()

    def blitMario(self):
        self.level.blit(self.image, self.rect)
