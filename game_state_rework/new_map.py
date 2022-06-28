import csv
import pygame
from pygame.locals import *


class Map:
    def __init__(self) -> None:
        self.image = '../img/map/rockMap80_80.png'
        self.offset = (592-96, 608-128)  # (canvas/2) to offset player image
        self.position = 0
        self.rendered = 0
        self.speed = .25
        self.boundaries = self.get_collisions()
        self.load()

    def load(self):
        self.rendered = pygame.image.load(self.image).convert_alpha()
        self.position = self.rendered.get_rect(
            topleft=(-self.offset[1], -self.offset[0]))

    def render(self):
        return self.rendered, self.position

    def get_collisions(self):
        collisionsMap = []
        with open('../data/rockMap/rockMap1_Collisions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                collisionsMap.append(row)
        boundaries = []
        for i, row in enumerate(collisionsMap):
            for j, tile in enumerate(row):
                if tile == '0':
                    boundaries.append(
                        Rect(j * 16 - (self.offset[1]), i * 16 - (self.offset[0]), 16, 16))
        return boundaries

    def update(self, direction, move):
        self.position = self.position.move(
            (direction)*move*16)
        for boundary in self.boundaries:
            boundary = boundary.move_ip(
                (direction)*move*16)
