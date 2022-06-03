import pygame
from pygame.locals import *


class Player:
    def __init__(self, screen_w, screen_h, fps):
        self.image = './img/PlayerDown_1.png'
        self.images_down = ['./img/PlayerDown_1.png',
                            './img/PlayerDown_2.png']
        self.position = Rect(screen_w / 2, screen_h / 2, 16, 16)
        self.rendered = 0
        self.direction = 'down'
        self.prev_direction = 'down'
        self.walking = False
        self.animate = False
        self.moving = False
        self.hold = int(fps/2)

    def update(self, hold_frames):
        print(hold_frames)
        # if animating, update image
        if self.animate:
            if self.direction == self.prev_direction:
                self.moving = True
            else:
                self.moving = False

            self.image = self.images_down[(hold_frames//self.hold)]

    def draw(self, mag, screen):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.rendered = pygame.transform.scale(
            self.rendered, (self.rendered.get_width()*mag, self.rendered.get_height()*mag))
        screen.blit(self.rendered, self.position)

    def animate_down():

        pass

    def reset(self):
        self.moving = False
        self.animate = False
        self.walking = False
        self.direction = 'down'
