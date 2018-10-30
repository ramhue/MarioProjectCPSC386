# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from stage_background import Stage_Background
from gameStats import GameStats
from mario import Mario
from goomba import Goomba


def Game():
    pygame.init()
    gamesettings = Settings()
    screen = pygame.display.set_mode((256 * gamesettings.scale, 224 * gamesettings.scale))
    pygame.display.set_caption("Super Mario")
    background = Stage_Background(screen)
    stats = GameStats(screen, gamesettings)
    player = Mario(screen, gamesettings)
    thegoomba = Goomba(screen, gamesettings)

    while True:
        gf.check_events(player, thegoomba, background)
        background.blitbackground()
        stats.blitstats()
        thegoomba.blitGoomba()
        player.blitMario()
        pygame.display.flip()

game = Game()
game.play()

