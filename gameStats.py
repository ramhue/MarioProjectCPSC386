# Displays game stats at top of screen
# Game stats includes Score, Coins, Time, Lives

import pygame

# Global Color
WHITE = (255, 255, 255)


class GameStats():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Score display text
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('images/ARCADECLASSIC.TTF', 36)
        self.Scores = self.font.render("SCORE", 2, WHITE)
        self.ScoresPos = self.Scores.get_rect()
        self.ScoresPos = (((self.settings.screen_width / 2) - 475), (self.settings.screen_height / 2) - 275)

        # Coins display text
        self.Coins = self.font.render("COINS", 2, WHITE)
        self.CoinsPos = self.Coins.get_rect()
        self.CoinsPos = ((self.settings.screen_width / 2) - 275, (self.settings.screen_height / 2) - 275)

        # Time display text
        self.Time = self.font.render("TIME", 2, WHITE)
        self.TimePos = self.Time.get_rect()
        self.TimePos = ((self.settings.screen_width / 2) - 75, (self.settings.screen_height / 2) - 275)

        # Lives display text
        self.Lives = self.font.render("LIVES", 2, WHITE)
        self.LivesPos = self.Lives.get_rect()
        self.LivesPos = ((self.settings.screen_width / 2) + 125, (self.settings.screen_height / 2) - 275)

    def blitstats(self):
        self.screen.blit(self.Scores, self.ScoresPos)
        self.screen.blit(self.Coins, self.CoinsPos)
        self.screen.blit(self.Time, self.TimePos)
        self.screen.blit(self.Lives, self.LivesPos)


