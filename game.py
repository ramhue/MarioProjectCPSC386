# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from stage_background import Stage_Background
from gameStats import GameStats
from mario import Mario
from goomba import Goomba

class Game():
    def __init__(self):
        pygame.init()
        self.scale = 3
        self.screen = pygame.display.set_mode((1024, 224 * self.scale))
        pygame.display.set_caption("Super Mario")

        self.gamesettings = Settings(self.screen)

        # Background Image for level
        self.background = pygame.image.load('images/marioW1.png')
        self.background = pygame.transform.scale(self.background, (self.background.get_width() * self.scale,
                                                                   self.background.get_height() * self.scale))
        self.rect = self.background.get_rect()
        # Create Surface called Level that will hold everythin
        # g within the level
        # (Player, enemy, background, colliders, items)
        self.level = pygame.Surface((self.rect.width, self.rect.height))

        self.player = Mario(self.screen, self.gamesettings, self.level)
        self.thegoomba = Goomba(self.level, self.gamesettings)
        self.stats = GameStats(self.screen, self.gamesettings)
        
    def play(self):
        while True:
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
        self.stats.blitstats()

        pygame.display.flip()


game = Game()
game.play()

