import pygame
import sys
from pygame.locals import*

pygame.init()

# What's needed for battle
monsters = {'geodude':
            {'name': 'GEODUDE',
             'image': './img/PlayerDown_1.png',
             'hp': 200,
             'moves': ['Tackle', 'Defense Curl']},
            'charmander':
            {'name': 'CHARMANDER',
             'image': 'somethingelse.png',
             'hp': 200},
            'moves': ['Tackle', 'Defense Curl']
            }


class Monster (pygame.sprite.Sprite):
    def __init__(self, monster):
        super().__init__()
        self.image = pygame.image.load(monster['image'])
        self.rect = self.image.get_rect()


friend = Monster(monsters['geodude'])

battle_monsters = pygame.sprite.Group()
battle_monsters.add(friend)


screen = pygame.display.set_mode((1088, 612))
pygame.display.set_caption("PokeGame")

running = True

while running:
    screen.fill((0, 0, 255))

    # check to end game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # display monster
    battle_monsters.draw(screen)

    # update
    pygame.display.update()

pygame.quit()
sys.exit()
