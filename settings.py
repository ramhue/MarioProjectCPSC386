# Settings for Super Mario


class Settings():
    def __init__(self, screen):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.scale = 3
        self.camera = self.screen.get_rect()
        self.camera.x = 0


