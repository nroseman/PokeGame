from pygame.locals import *


class Player:
    def __init__(self, image, screen_w, screen_h):
        self.image = image
        self.position = Rect(screen_w / 2, screen_h / 2, 16, 16)
