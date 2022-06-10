import pygame
from pygame.locals import *


def start(screen, screen_width, screen_height):
    menu_button = pygame.image.load('./img/press_start.png')
    screen.blit(menu_button, (screen_width / 2, screen_height / 2, 120, 16))
