# Mario player class

import pygame
from settings import Settings
from pygame.sprite import Sprite
from spritesheet import SpriteSheet

class Mario(Sprite):
    def __init__(self, screen, settings, level, death=False):
        super(Mario, self).__init__()
        self.last = pygame.time.get_ticks()
        self.screen = screen
        self.settings = settings
        self.level = level
        self.spritesheet = SpriteSheet('images/mario.png')
        self.smallimages = list()
        self.bigimages = list()
        self.animator = 0
        for x in range(14):
            self.smallimages.append(self.spritesheet.get_image(80+(x*17), 34, 16, 16))
            self.smallimages[x] = pygame.transform.scale(self.smallimages[x],
                                                         (self.smallimages[x].get_width()*self.settings.scale,
                                                         self.smallimages[x].get_height()*self.settings.scale))

        self.image = self.smallimages[0]
        self.rect = self.image.get_rect()

        self.image = self.smallimages[0]
        self.rect = self.image.get_rect()

        # Set starting Y:
        self.rect.y = 250

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.jumping = False
        self.Falling = False

        #STATE Flag
        self.face_right = True
        self.face_left = False
        self.dead = False
        self.Star = False
        self.big = False
        self.fire_mario = False
        self.ducking = False
        self.state_list = ["Stand", "Walk", "Jumping" "Run",
                           "Duck", "FaceLeft", "FaceRight",
                           "Falling"]
        self.current_state = "Stand"

        #Forces
        self.vel_x = 0
        self.vel_y = self.settings.gravity
        self.vel_x_Max = 50
        self.vel_y_Max = 10

        self.walk_accel_x = .5
        self.gravity = 1
        self.gravity_jump = .5
        self.vel_jump = 10
        self.run_accel_x = 20
        self.RUN_MAX = 80
        self.MAX_WALK = 3
        self.run_walk_vel = -13

        # TEMPORARY: Flag to check if camera is moving
        self.cameraMove = False

        # Collision with enemies
        self.death = False

    def update(self):
        super().update()
        if self.moveRight:
            if self.vel_x < self.MAX_WALK:
                self.vel_x += self.walk_accel_x

        if self.moveLeft:
            if self.vel_x > (self.MAX_WALK * -1):
                self.vel_x -= self.walk_accel_x
                if self.vel_x > -1:
                    self.vel_x = -1
            elif self.vel_x < (self.MAX_WALK * -1):
                self.vel_x += self.walk_accel_x

        if self.jumping == True:
            self.image = self.smallimages[5]
            if self.face_left:
                self.image = pygame.transform.flip(self.image, True, False)
            if self.vel_y < 0:
                self.vel_y += 1
            elif self.vel_y == 0:
                self.vel_y = -1
                self.jumping = False
                self.Falling = True

        elif self.Falling:
            if self.vel_y > self.settings.gravity:
                self.vel_y -= 1
            elif self.vel_y == self.settings.gravity:
                self.Falling = False
                self.image = self.smallimages[0]

        print(str(self.vel_y))
        self.rect.x += round(self.vel_x)
        self.rect.y -= round(self.vel_y)

        if self.settings.camera.x < self.rect.x - self.settings.screen_width/2:
            self.settings.camera.x += self.vel_x

    def reset(self):
        self.rect.x, self.rect.y = 0, 550
        self.image = self.smallimages[0]

    def blitMario(self):
        if self.moveRight:
            self.face_left = False
            self.face_right = True
            if pygame.time.get_ticks() > self.last + 100:
                if self.animator == 3:
                    self.animator = 0
                else:
                    self.animator += 1
                self.image = self.smallimages[self.animator]
                self.last = pygame.time.get_ticks()
        if self.moveLeft:
            self.face_left = True
            self.face_right = False
            if pygame.time.get_ticks() > self.last + 200:
                if self.animator == 3:
                    self.animator = 0
                else:
                    self.animator += 1
                self.image = self.smallimages[self.animator]
                self.image = pygame.transform.flip(self.image, True, False)
                self.last = pygame.time.get_ticks()
        if self.moveRight is False and self.moveLeft is False:
            if self.face_left:
                self.image = pygame.transform.flip(self.image, True, False)
            self.image = self.smallimages[0]

        if self.death:
            self.image = self.smallimages[6]
            if pygame.time.get_ticks() > self.last + 200:
                self.reset()
            self.death = False

        self.level.blit(self.image, self.rect)
