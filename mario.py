# Mario player class

import pygame
from settings import Settings
from pygame.sprite import Sprite
from spritesheet import SpriteSheet

class Mario(Sprite):
    def __init__(self, screen, settings, level):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.level = level
        self.spritesheet = SpriteSheet('images/mario.png')
        self.smallimages = list()
        for x in range(14):
            self.smallimages.append(self.spritesheet.get_image(80+(x*17), 34, 16, 16))
            self.smallimages[x] = pygame.transform.scale(self.smallimages[x],
                                                         (self.smallimages[x].get_width()*self.settings.scale,
                                                         self.smallimages[x].get_height()*self.settings.scale))
        self.image = self.smallimages[0]
        self.rect = self.image.get_rect()

        # Set starting Y:
        self.rect.y = 550

        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        self.jumping = False
        self.Falling = False

        #STATE Flags
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
        self.vel_y = 0
        self.vel_x_Max = 5
        self.vel_y_Max = -10
        self.walk_accel_x = .2
        self.gravity = 1
        self.gravity_jump = .5
        self.vel_jump = 10
        self.run_accel_x = 20
        self.RUN_MAX = 80
        self.MAX_WALK = 3
        self.run_walk_vel = -13


        # TEMPORARY: Flag to check if camera is moving
        self.cameraMove = False

    def update(self):
        super().update()
        if self.moveRight:
            if self.vel_x < self.MAX_WALK:
                self.vel_x += self.walk_accel_x

        if self.cameraMove:
            self.settings.camera.x += round(self.vel_x)

        if self.moveLeft:
            if self.vel_x > (self.MAX_WALK * -1):
                self.vel_x -= self.walk_accel_x
                if self.vel_x > -.5:
                    self.vel_x = -.5
            elif self.vel_x < (self.MAX_WALK * -1):
                self.vel_x += self.walk_accel_x

        if self.jumping == True:
            print('HELLO')
            print(str(self.vel_y ))
            if self.vel_y < self.vel_y_Max:
                self.vel_y += self.gravity_jump
                print(str(self.vel_y))
                self.rect.y -= round(self.vel_y)
            if self.vel_y == self.vel_y_Max:
                self.Falling = True
        elif self.Falling == True:
                self.vel_y -= self.gravity
                self.rect.y += round(self.vel_y)
                if self.vel_y == 0:
                    self.Falling = False

        self.rect.x += round(self.vel_x)

       # if self.Falling:
        #if self.current_state = "Stand"


    def blitMario(self):
        self.level.blit(self.image, self.rect)
    def cameraCheck(self):
        if self.rect.x == self.settings.camera.x + (self.settings.screen_width/2):
            print(self.settings.camera.x + (self.settings.screen_width/2))
            self.cameraMove = True


