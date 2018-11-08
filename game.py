# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from stage_background import Stage_Background
from gameStats import GameStats
from mario import Mario
from goomba import Goomba
from koopa import Koopa
from pygame.sprite import Group
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

        # Add mario to the game
        self.player = Mario(self.screen, self.gamesettings, self.level)

        # Add all goombas
        self.thegoomba = Group()
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 352, 220))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 640, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 815, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 840, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1280, 55))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1310, 55))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1555, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1580, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1820, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1842, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 1985, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 2008, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 2045, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 2068, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 2785, 184))
        self.thegoomba.add(Goomba(self.level, self.gamesettings, 2808, 184))

        # Add koopa
        self.thekoopa = Group()
        self.thekoopa.add(Koopa(self.level, self.gamesettings, 1717, 178))

        # Game stats
        self.stats = GameStats(self.screen, self.gamesettings)

        # Stage objects
        self.pipes = Group()
        self.ground = Group()
        self.steps = Group()
        self.createblocks()
        
    def play(self):
        while True:
            # CHANGE TO MARIO
            gf.check_events(self.player, self.thegoomba, self.background)
            self.checkCollision()
            self.checkGoombaCollision()
            self.checkKoopaCollision()
            # self.background.blitbackground()
            self.blit()

    # Blit everything to self.level then blit self.level
    def blit(self):
        self.level.blit(self.background, self.gamesettings.camera, self.gamesettings.camera)
        for goomba in self.thegoomba:
            goomba.blitGoomba()
        for koopa in self.thekoopa:
            koopa.blitKoopa()
        self.player.update()
        self.thegoomba.update()
        self.thekoopa.update()

        # DEBUG
        # self.pipes.draw(self.level)
        # self.ground.draw(self.level)
        # self.steps.draw(self.level)
        # /DEBUG
        self.screen.blit(self.level, (0, 0), self.gamesettings.camera)

        self.stats.blitstats()

        pygame.display.flip()

    def checkCollision(self):
        collided = pygame.sprite.spritecollide(self.player, self.pipes, False, False)
        for pipe in collided:
            self.player.rect.bottom = pipe.rect.top

        collided = pygame.sprite.spritecollide(self.player, self.steps, False, False)
        for step in collided:
            self.player.rect.bottom = step.rect.top

        collided = pygame.sprite.spritecollide(self.player, self.ground, False, False)
        for ground in collided:
            self.player.rect.bottom = ground.rect.top


    def checkGoombaCollision(self):
        collided = pygame.sprite.groupcollide(self.thegoomba, self.pipes, False, False)
        for goomba, pipe in collided.items():
            #goomba.rect.bottom = pipe[0].rect.top
            if pipe[0].rect.x < goomba.rect.x:
                goomba.moveLeft = False
            if pipe[0].rect.x > goomba.rect.x:
                goomba.moveLeft = True

        collided = pygame.sprite.groupcollide(self.thegoomba, self.steps, False, False)
        for goomba, step in collided.items():
            goomba.rect.bottom = step[0].rect.top

        collided = pygame.sprite.groupcollide(self.thegoomba, self.ground, False, False)
        for goomba, ground in collided.items():
            goomba.rect.bottom = ground[0].rect.top

    def checkKoopaCollision(self):
        collided = pygame.sprite.groupcollide(self.thekoopa, self.pipes, False, False)
        for koopa, pipe in collided.items():
                # goomba.rect.bottom = pipe[0].rect.top
            if pipe[0].rect.x < koopa.rect.x:
                  koopa.moveLeft = False
            if pipe[0].rect.x > koopa.rect.x:
                  koopa.moveLeft = True

        collided = pygame.sprite.groupcollide(self.thekoopa, self.steps, False, False)
        for koopa, step in collided.items():
            koopa.rect.bottom = step[0].rect.top

        collided = pygame.sprite.groupcollide(self.thekoopa, self.ground, False, False)
        for koopa, ground in collided.items():
            koopa.rect.bottom = ground[0].rect.top

    def createblocks(self):
        # Create Pipes
        self.pipes.add(blockRect(447, 166, 32, 32, self.gamesettings.scale)) # Pipe 1
        self.pipes.add(blockRect(607, 150, 32, 48, self.gamesettings.scale)) # Pipe 2
        self.pipes.add(blockRect(735, 134, 32, 64, self.gamesettings.scale)) # Pipe 3
        self.pipes.add(blockRect(911, 134, 32, 64, self.gamesettings.scale)) # Pipe 4
        self.pipes.add(blockRect(2607, 166, 32, 32, self.gamesettings.scale)) # Pipe 5
        self.pipes.add(blockRect(2863, 166, 32, 32, self.gamesettings.scale)) # Pipe 6

        # Create ground
        self.ground.add(blockRect(0, 198, 1103, 24, self.gamesettings.scale))
        self.ground.add(blockRect(1135, 198, 240, 24, self.gamesettings.scale))
        self.ground.add(blockRect(1423, 198, 1024, 24, self.gamesettings.scale))
        self.ground.add(blockRect(2479, 198, 912, 24, self.gamesettings.scale))

        # Create steps
        self.steps.add(blockRect(2143, 182, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2159, 166, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2175, 150, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2191, 134, 16, 64, self.gamesettings.scale))

        self.steps.add(blockRect(2239, 134, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2239+16, 134+16, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2239+32, 134+32, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2239+48, 134+48, 16, 16, self.gamesettings.scale))

        self.steps.add(blockRect(2367, 182, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2367+16, 182-16, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2367+32, 182-32, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2367+48, 182-48, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2367+64, 182-48, 16, 64, self.gamesettings.scale))

        self.steps.add(blockRect(2479, 134, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2479+16, 134+16, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2479+32, 134+32, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2479+48, 134+48, 16, 16, self.gamesettings.scale))

        self.steps.add(blockRect(2895, 182, 16, 16, self.gamesettings.scale))
        self.steps.add(blockRect(2895+16, 182-16, 16, 32, self.gamesettings.scale))
        self.steps.add(blockRect(2895+32, 182-32, 16, 48, self.gamesettings.scale))
        self.steps.add(blockRect(2895+48, 182-48, 16, 64, self.gamesettings.scale))
        self.steps.add(blockRect(2895+64, 182-64, 16, 80, self.gamesettings.scale))
        self.steps.add(blockRect(2895+80, 182-80, 16, 96, self.gamesettings.scale))
        self.steps.add(blockRect(2895+96, 182-96, 16, 112, self.gamesettings.scale))
        self.steps.add(blockRect(2895+112, 182-112, 16, 128, self.gamesettings.scale))
        self.steps.add(blockRect(2895+128, 182-112, 16, 128, self.gamesettings.scale))


game = Game()
game.play()

