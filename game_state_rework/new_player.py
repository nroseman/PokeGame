import pygame
from pygame.locals import *


class Player:
    def __init__(self, canvas):
        self.image = '../img/player/PlayerDown_1.png'
        # 1 - Left, 2 - Right, 3 - Down, 4 - Up
        self.canvas = canvas
        self.images = [
            ['./img/player/PlayerDown_1.png', './img/player/PlayerDown_2.png',
                './img/player/PlayerDown_3.png'],
            ['img/player/playerLeft0.png', 'img/player/playerLeft1.png',
                'img/player/playerLeft2.png'],
            ['img/player/playerRight0.png', 'img/player/playerRight1.png',
                'img/player/playerRight2.png'],
            ['img/player/playerUp0.png', 'img/player/playerUp1.png',
                'img/player/playerUp2.png']
        ]
        self.position = Rect(canvas.get_width() / 2,
                             canvas.get_height() / 2, 16, 16)
        self.rendered = 0
        self.direction = 0
        self.animate = False
        self.moving = False
        self.load()
        self.hitboxes = self.load_hitboxes()

    def load(self):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.position = self.rendered.get_rect(bottomleft=(
            self.canvas.get_width() / 2, (self.canvas.get_height() / 2) + (self.rendered.get_height() / 2)))

    def load_hitboxes(self):
        hitboxes = {
            'left': Rect(self.position.left - (16), self.position.top + (16), 16, 16),
            'right': Rect(self.position.left + (16), self.position.top + (16), 16, 16),
            'up': Rect(self.position.left, self.position.top, 16, 16),
            'down': Rect(self.position.left, self.position.top + (16 * 2), 16, 16),
        }
        return hitboxes

    def is_moving(self):
        if (self.direction == self.prev_direction) and self.walking:
            self.moving = 1
            return True
        else:
            self.moving = 0
            return False

    def update(self):
        # if animating, update image
        if self.animate:
            self.image = self.images[self.direction][self.step + 1]

    def render(self):
        # self.rendered.fill((255, 0, 0))
        return self.rendered, self.position

    def animate_down():

        pass

    def reset(self):
        self.moving = 0
        self.animate = False
        self.walking = False
        self.prev_direction = self.direction
        self.image = self.images[self.direction][0]
        self.step = int(not self.step)
