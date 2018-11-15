# Mario game functions

import pygame
import sys


def check_events(mario, goomba, background):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)


def check_keydown_events(event, mario):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        mario.moving_up = True
        mario.cameraMove = True
    if event.key == pygame.K_LSHIFT:
        mario.running = True
    elif event.key == pygame.K_SPACE:
        mario.jumping = True
    elif event.key == pygame.K_DOWN:
        mario.moving_down = True
    elif event.key == pygame.K_RIGHT:
        mario.moveRight = True
    elif event.key == pygame.K_LEFT:
        mario.moveLeft = True
        mario.current_state = mario.state_list[1]
    elif event.key == pygame.K_QUIT:
        sys.exit()


def check_keyup_events(event, mario):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
        mario.moveRight = False
    elif event.key == pygame.K_LEFT:
        mario.moveLeft = False
    elif event.key == pygame.K_UP:
        mario.moving_up = False
        mario.cameraMove = False
    elif event.key == pygame.K_DOWN:
        mario.moving_down = False
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.K_LSHIFT:
        mario.running = False

    mario.vel_x = 0


