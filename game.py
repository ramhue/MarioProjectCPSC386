import pygame
from spritesheet import SpriteSheet

class Game():

    def __init__(self):

        self.scale = 3

        pygame.init()
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width()*self.scale,
                                                                   self.background.get_height()*self.scale))
        self.screen = pygame.display.set_mode((256*self.scale, 224*self.scale))

        self.camera = self.screen.get_rect()
        self.camera.x = 0

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.camera.x += 10*self.scale
                    elif event.key == pygame.K_LEFT:
                        self.camera.x -= 10*self.scale
            self.screen.blit(self.background, (0, 0), self.camera)
            pygame.display.flip()


game = Game()
game.play()