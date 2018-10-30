import pygame
from spritesheet import SpriteSheet

class Game():

    def __init__(self):

        self.scale = 3

        pygame.init()
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width()*self.scale,
                                                                   self.background.get_height()*self.scale))
        self.backrect = self.background.get_rect()
        # self.backrect.x -= 400*self.scale
        self.screen = pygame.display.set_mode((256*self.scale, 224*self.scale))

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.backrect.x -= 10*self.scale
                    elif event.key == pygame.K_LEFT:
                        self.backrect.x += 10*self.scale
            self.screen.blit(self.background, self.backrect)
            pygame.display.flip()


game = Game()
game.play()