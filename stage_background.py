# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Mario background

import pygame


class Stage_Background():
    def __init__(self, screen):
        self.screen = screen
        #self.width = 1920
        #self.height = 576
        self.scale = 3
        img = pygame.image.load('images/marioW1.png')
        img = pygame.transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
        self.rect = img.get_rect()
        #self.rect.x -= 400 * self.scale
        self.image = img

    def blitbackground(self):
        self.screen.blit(self.image, self.rect)