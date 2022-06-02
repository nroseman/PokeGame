import pygame
from pygame.locals import *


class Player:
    def __init__(self, screen_w, screen_h):
        self.image = './img/PlayerOD.png'
        self.images_down = ['./img/PlayerOD.png',
                            './img/PlayerOD_Walk_Down.png']
        self.position = Rect(screen_w / 2, screen_h / 2, 16, 16)
        self.rendered = 0

    def draw(self, mag):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.rendered = pygame.transform.scale(
            self.rendered, (self.rendered.get_width()*mag, self.rendered.get_height()*mag))
        return

    def go_down():

        pass
