# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from stage_background import Stage_Background
from mario import Mario
from goomba import Goomba

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
BLUE = (132, 112, 255)


class Game():
    def __init__(self):
        pygame.init()
        self.scale = 3
        self.screen = pygame.display.set_mode((256 * self.scale, 224 * self.scale))
        self.gamesettings = Settings(self.screen)
        pygame.display.set_caption("Super Mario")
        # self.background = Stage_Background(self.screen)
        self.background = pygame.image.load('images/marioW1.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width() * self.scale,
                                                                   self.background.get_height() * self.scale))
        self.rect = self.background.get_rect()
        self.level = pygame.Surface((self.rect.width, self.rect.height))
        self.player = Mario(self.level, self.gamesettings)
        self.thegoomba = Goomba(self.level, self.gamesettings)
        self.screen.fill(BLACK)

    def play(self):
        while True:
            self.screen.fill(BLACK)
            # CHANGE TO MARIO
            gf.check_events(self.player, self.thegoomba, self.background)
            # self.background.blitbackground()
            self.blit()

    # Blit everything to self.level then blit self.level
    def blit(self):
        self.level.blit(self.background, self.gamesettings.camera, self.gamesettings.camera)
        self.thegoomba.blitGoomba()
        self.player.update()
        self.screen.blit(self.level, (0, 0), self.gamesettings.camera)
        pygame.display.flip()


game = Game()
game.play()

