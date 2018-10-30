# Aaron Xaymountry
# CPSC 386-01
# MW 5:30-6:45pm
# Mario game functions

import pygame
import sys
from stage_background import Stage_Background
from pygame.sprite import Group


def check_events(mario, goomba, background):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario, goomba, background)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mario)

def check_keydown_events(event, mario, goomba, background):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        mario.moving_up = True
    elif event.key == pygame.K_DOWN:
        mario.moving_down = True
    elif event.key == pygame.K_RIGHT:
        mario.moving_right = True
        #if background.rect
        #goomba.pos1 = (background.scale * 10)
        #goomba.pos2 -= (background.scale * 10)
        goomba.rect.x -= (background.scale * 10)

        background.rect.x -= (background.scale * 10)
    elif event.key == pygame.K_LEFT:
        mario.moving_left = True
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.K_QUIT:
        sys.exit()


def check_keyup_events(event, mario):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        mario.moving_right = False
    elif event.key == pygame.K_LEFT:
        mario.moving_left = False
    elif event.key == pygame.K_UP:
        mario.moving_up = False
    elif event.key == pygame.K_DOWN:
        mario.moving_down = False


# Check direction mario is going to compare and see if he can't go a direction anymore if he hit a block
def check_direction(mario, block):
    left = False
    right = False
    up = False
    down = False
    if mario.rect.centerx <= block.rect.centerx:
        right = True
    else:
        left = True
    if mario.rect.y + mario.rect.height / 2 <= block.rect.y + block.rect.height / 2:
        up = True
    else:
        down = True

    if left:
        mario.x += 1
    elif right:
        mario.x -= 1
    if up:
        mario.y -= 1
    elif down:
        mario.y += 1


# Mario collision handling
def check_collision(mario, blocks):
    for block in blocks:
        if pygame.sprite.collide_rect(mario, block):
            print("collided")
            check_direction(mario, block)


