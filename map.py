import csv
import pygame
from pygame.locals import *


class Map:
    def __init__(self, mag, screen_width, screen_height, tile_size) -> None:
        self.image = './img/map/rockMap80_80.png'
        self.width = 80
        self.height = 80
        self.offset = ((36 * tile_size) - (screen_height /
                       2), (38 * tile_size) - (screen_width /
                       2))  # (screen/2) to offset player image
        self.position = 0
        self.rendered = 0

    def load(self, tile_size, screen_width):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.rendered = pygame.transform.scale(
            self.rendered, (self.height*tile_size, self.width*tile_size))
        self.position = self.rendered.get_rect(
            topleft=(-self.offset[1], -self.offset[0]))

    def render(self, surface):
        surface.blit(self.rendered, self.position)

    def collisions(self, tile_size):
        collisionsMap = []
        with open('./data/rockMap/rockMap1_Collisions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                collisionsMap.append(row)
        boundaries = []
        for i, row in enumerate(collisionsMap):
            for j, tile in enumerate(row):
                if tile == '0':
                    boundaries.append(
                        Rect(j * tile_size - (self.offset[1]), i * tile_size - (self.offset[0]), tile_size, tile_size))
        return boundaries
