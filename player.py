import pygame
from pygame.locals import *


class Player:
    def __init__(self, screen_w, screen_h, fps):
        self.image = './img/PlayerDown_1.png'
        # 0 - Down, 1 - Left, 2 - Right, 3 - Up
        self.images = [
            ['./img/PlayerDown_1.png', './img/PlayerDown_2.png'],
            ['img/playerLeft0.png', 'img/playerLeft1.png'],
            ['img/playerRight0.png', 'img/playerRight1.png'],
            ['img/playerUp0.png', 'img/playerUp1.png']
        ]
        self.position = Rect(screen_w / 2, screen_h / 2, 16, 16)
        self.rendered = 0
        self.direction = 0
        self.prev_direction = 0
        self.walking = False
        self.animate = False
        self.moving = 0
        self.hold = 2

    def is_moving(self):
        if (self.direction == self.prev_direction) and self.walking:
            self.moving = 1
            return True
        else:
            self.moving = 0
            return False

    def update(self, hold_frames):
        # if animating, update image
        if self.animate:
            self.image = self.images[self.direction][hold_frames % 2]

    def draw(self, mag, screen):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.rendered = pygame.transform.scale(
            self.rendered, (self.rendered.get_width()*mag, self.rendered.get_height()*mag))
        screen.blit(self.rendered, self.position)

    def animate_down():

        pass

    def reset(self):
        self.moving = 0
        self.animate = False
        self.walking = False
        self.prev_direction = self.direction
        self.image = self.images[self.direction][0]
