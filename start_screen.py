import pygame


# Global Color
WHITE = (255, 255, 255)


class Start_Screen():
    def __init__(self, screen, settings):
        pygame.init()
        self.screen = screen
        self.settings = settings

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # World Background
        self.scale = 3
        img = pygame.image.load('images/marioW1.png')
        img = pygame.transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale))
        self.rect = img.get_rect()
        self.image = img

        # Super Mario Bros. Rectangle in middle of screen
        self.x = (self.settings.screen_width / 2) - 275
        self.y = (self.settings.screen_height / 2) - 250
        self.width = 550
        self.height = 300
        boximg = pygame.image.load('images/SuperMarioBrosRec.png')
        boximg = pygame.transform.scale(boximg, (self.width, self.height))
        self.boxrect = boximg.get_rect()
        self.boxrect.x, self.boxrect.y = self.x, self.y
        self.boximage = boximg

        # Score display text
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('images/ARCADECLASSIC.TTF', 36)
        self.Scores = self.font.render("SCORE", 2, WHITE)
        self.ScoresPos = self.Scores.get_rect()
        self.ScoresPos = (((self.settings.screen_width / 2) - 475), (self.settings.screen_height / 2) - 325)

        # Coins display text
        self.Coins = self.font.render("COINS", 2, WHITE)
        self.CoinsPos = ((self.settings.screen_width / 2) - 200, (self.settings.screen_height / 2) - 325)

        # Time display text
        self.Time = self.font.render("TIME", 2, WHITE)
        self.TimePos = ((self.settings.screen_width / 2) + 100, (self.settings.screen_height / 2) - 325)

        # Lives display text
        self.Lives = self.font.render("LIVES", 2, WHITE)
        self.LivesPos = ((self.settings.screen_width / 2) + 375, (self.settings.screen_height / 2) - 325)

        # Display Play button
        #self.font.size(100)
        self.font2 = pygame.font.Font('images/ARCADECLASSIC.TTF', 56)
        self.Play = self.font2.render("PLAY GAME", 2, WHITE)
        self.PlayPos = ((self.settings.screen_width / 2) - 125, (self.settings.screen_height / 2) + 75)


    def blit(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.Scores, self.ScoresPos)
        self.screen.blit(self.Coins, self.CoinsPos)
        self.screen.blit(self.Time, self.TimePos)
        self.screen.blit(self.Lives, self.LivesPos)
        self.screen.blit(self.Play, self.PlayPos)
        self.screen.blit(self.boximage, self.boxrect)


