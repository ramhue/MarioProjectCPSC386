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


def Game():
    pygame.init()
    gamesettings = Settings()
    scale = 3
    screen = pygame.display.set_mode((256 * scale, 224 * scale))
    pygame.display.set_caption("Super Mario")
    background = Stage_Background(screen)
    player = Mario(screen, gamesettings)
    thegoomba = Goomba(screen, gamesettings)
    screen.fill(BLACK)

    while True:
        screen.fill(BLACK)
        # CHANGE TO MARIO
        gf.check_events(player, thegoomba, background)
        background.blitbackground()
        thegoomba.blitGoomba()
        player.blitMario()
        pygame.display.flip()

game = Game()
game.play()

