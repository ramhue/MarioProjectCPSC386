# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from stage_background import Stage_Background
from gameStats import GameStats
from mario import Mario
from goomba import Goomba
from pygame.sprite import Group
from blockrect import blockRect

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

        self.pipes = Group()
        self.ground = Group()
        self.steps = Group()
        self.createblocks()
        
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

        self.pipes.draw(self.level)
        self.ground.draw(self.level)
        self.steps.draw(self.level)
        self.screen.blit(self.level, (0, 0), self.gamesettings.camera)

        self.stats.blitstats()

        pygame.display.flip()

    def createblocks(self):
        # Create Pipes
        self.pipes.add(blockRect(447, 168, 32, 32, self.gamesettings.scale)) # Pipe 1
        self.pipes.add(blockRect(607, 152, 32, 48, self.gamesettings.scale)) # Pipe 2
        self.pipes.add(blockRect(735, 136, 32, 64, self.gamesettings.scale)) # Pipe 3
        self.pipes.add(blockRect(911, 136, 32, 64, self.gamesettings.scale)) # Pipe 4
        self.pipes.add(blockRect(2607, 168, 32, 32, self.gamesettings.scale)) # Pipe 5
        self.pipes.add(blockRect(2863, 168, 32, 32, self.gamesettings.scale)) # Pipe 6

        # Create ground
        self.ground.add(blockRect(0, 200, 1103, 24, self.gamesettings.scale))
        self.ground.add(blockRect(1135, 200, 240, 24, self.gamesettings.scale))
        self.ground.add(blockRect(1423, 200, 1024, 24, self.gamesettings.scale))
        self.ground.add(blockRect(2479, 200, 912, 24, self.gamesettings.scale))

        # Create steps
        self.steps.add(blockRect(2143, 184, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2159, 168, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2175, 152, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2191, 136, 16, 64, self.gamesettings.scale))

        self.steps.add(blockRect(2239, 136, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2239+16, 136+16, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2239+32, 136+32, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2239+48, 136+48, 16, 16, self.gamesettings.scale))

        self.steps.add(blockRect(2367, 184, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2367+16, 184-16, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2367+32, 184-32, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2367+48, 184-48, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2367+64, 184-48, 16, 64, self.gamesettings.scale))

        self.steps.add(blockRect(2479, 136, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2479+16, 136+16, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2479+32, 136+32, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2479+48, 136+48, 16, 16, self.gamesettings.scale))

        self.steps.add(blockRect(2895, 184, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2895+16, 184-16, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2895+32, 184-32, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2895+48, 184-48, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2895+64, 184-64, 16, 80, self.gamesettings.scale))
        self.steps.add(blockRect(2895+80, 184-80, 16, 96, self.gamesettings.scale))
        self.steps.add(blockRect(2895+96, 184-96, 16, 112, self.gamesettings.scale))
        self.steps.add(blockRect(2895+112, 184-112, 16, 128, self.gamesettings.scale))
        self.steps.add(blockRect(2895+128, 184-112, 16, 128, self.gamesettings.scale))


game = Game()
game.play()

