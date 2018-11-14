# Mario Game main function

import pygame
import game_functions as gf
from settings import Settings
from start_screen import Start_Screen
from gameStats import GameStats
from mario import Mario
from goomba import Goomba
from koopa import Koopa
from pygame.sprite import Group
from blockrect import blockRect
from floatBlock import FloatBlock

class Game():
    def __init__(self):
        pygame.init()
        self.scale = 3
        self.screen = pygame.display.set_mode((1024, 224 * self.scale))
        pygame.display.set_caption("Super Mario")

        self.gamesettings = Settings(self.screen)

        # Start Screen
        self.startscreen = Start_Screen(self.screen, self.gamesettings)

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

        # Add all goombas to game
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

        # Add koopa to game
        self.thekoopa = Group()
        self.thekoopa.add(Koopa(self.level, self.gamesettings, 1717, 178))

        # Game stats
        self.stats = GameStats(self.screen, self.gamesettings)

        # Stage objects
        self.pipes = Group()
        self.ground = Group()
        self.steps = Group()
        self.coinBlocks = Group()
        self.brickBlocks = Group()
        self.createblocks()

    def intro(self):
        self.startscreen.blit()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def play(self):
        self.intro()
        while True:
            # CHANGE TO MARIO
            gf.check_events(self.player, self.thegoomba, self.background)
            self.update()
            self.checkCollision()
            self.checkGoombaCollision()
            self.checkKoopaCollision()
            self.blit()

    # Blit everything to self.level then blit self.level
    def blit(self):
        self.startscreen.blit()
        self.level.blit(self.background, self.gamesettings.camera, self.gamesettings.camera)
        for goomba in self.thegoomba:
            goomba.blitGoomba()
        for koopa in self.thekoopa:
            koopa.blitKoopa()
        self.player.blitMario()
        self.player.update()
        self.thegoomba.update()
        self.thekoopa.update()
        # DEBUG
        # self.pipes.draw(self.level)
        # self.ground.draw(self.level)
        # self.steps.draw(self.level)
        # /DEBUG
        self.coinBlocks.draw(self.level)
        self.brickBlocks.draw(self.level)
        self.startscreen.blit()
        self.screen.blit(self.level, (0, 0), self.gamesettings.camera)
        self.stats.blitstats()
        pygame.display.flip()

    # Mario collision check with game objects and enemies
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

        collided = pygame.sprite.spritecollide(self.player, self.coinBlocks, False, False)
        for brick in collided:
            brick.movingUp = True
        collided = pygame.sprite.spritecollide(self.player, self.brickBlocks, False, False)
        for brick in collided:
            brick.movingUp = True

        # Check mario collisions with enemies
        # if collide by side mario dies or loses 1 level
        # Mario will kill enemies if he jumps on them
        collided = pygame.sprite.spritecollide(self.player, self.thegoomba, False, False)
        for goomba in collided:
            if self.player.rect.x >= goomba.rect.x:
                self.player.death = True
                self.player.rect.y -= self.gamesettings.gravity * 2

        collided = pygame.sprite.spritecollide(self.player, self.thegoomba, True, False)
        for goomba in collided:
            if self.player.rect.bottom == goomba.rect.top:
                goomba.death = True

        collided = pygame.sprite.spritecollide(self.player, self.thekoopa, False, False)
        for koopa in collided:
            if self.player.rect.x >= koopa.rect.x:
                self.player.death = True
                self.player.rect.y -= self.gamesettings.gravity
            if self.player.rect.bottom >= koopa.rect.top:
                koopa.death = True

    def checkGoombaCollision(self):
        collided = pygame.sprite.groupcollide(self.thegoomba, self.pipes, False, False)
        for goomba, pipe in collided.items():
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

        # Create floating coin blocks
        self.coinBlocks.add(FloatBlock(255, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(333, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(333+32, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(351, 72, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1247, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1503, 72, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1695, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1743, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1743, 72, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(1791, 136, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(2063, 72, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(2063+16, 72, 16, 16, 80, 112, self.gamesettings.scale))
        self.coinBlocks.add(FloatBlock(2719, 136, 16, 16, 80, 112, self.gamesettings.scale))

        # Create floating brick blocks
        self.brickBlocks.add(FloatBlock(317, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(317+32, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(317+64, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1231, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1231+32, 136, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(1279, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+16, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+32, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+48, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+64, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+80, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+96, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1279+112, 72, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(1455, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1455+16, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1455+32, 72, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(1503, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1599, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1599+16, 136, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(1887, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1935, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1935+16, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(1935+32, 72, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(2047, 72, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(2047+48, 72, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(2063, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(2063+16, 136, 16, 16, 272, 112, self.gamesettings.scale))

        self.brickBlocks.add(FloatBlock(2687, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(2687+16, 136, 16, 16, 272, 112, self.gamesettings.scale))
        self.brickBlocks.add(FloatBlock(2687+48, 136, 16, 16, 272, 112, self.gamesettings.scale))





































    def update(self):
        self.checkCollision()
        self.player.update()
        for brick in self.coinBlocks:
            brick.update()
        for brick in self.brickBlocks:
            brick.update()


game = Game()
game.play()

