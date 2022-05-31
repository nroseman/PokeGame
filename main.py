# TODO: add collision detection  --done
# TODO: add stop for collision
# TODO: make player class/refactor code/declutter main game loop
# TODO: add map transitions for buildings/new map segments
# TODO: scale up images (without messing with Rects and movement)

import pygame
from pygame.locals import *
import csv

frame = 1
scale = 16
mag = 4
size = width, height = (40 * scale, 40 * scale)


pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PokeGame")
# set background color
screen.fill((20, 200, 50))


# apply changes
pygame.display.update()

# load images
background = pygame.image.load("./img/testMap.png").convert()
background = pygame.transform.scale(
    background, (background.get_width(), background.get_height()))
background_loc = background.get_rect()
# background_loc.center = width/2, height/2
player = pygame.image.load("./img/PlayerOD.png").convert_alpha()

# to get one slice of animation from image
# player1 = player.subsurface(0, 0, player.get_width()/4, player.get_height())

player = pygame.transform.scale(
    player, (player.get_width(), player.get_height()))
player_loc = player.get_rect(bottomleft=(width/2, height/2))
player_hitbox = Rect(player_loc.left, player_loc.top + 16, 16, 16)
# player1_loc.center = width/2, height/2

# Add collisions from csv file
collisionsMap = []
with open('./data/testmapLayers_Collision.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        collisionsMap.append(row)
boundaries = []
for i, row in enumerate(collisionsMap):
    for j, tile in enumerate(row):
        if tile == '0':
            boundaries.append(Rect(j * scale, i * scale, scale, scale))

print(boundaries)

while running:
    screen.fill((20, 200, 50))
    # change frame rate
    # clock = pygame.time.Clock()
    # clock.tick(1)
    # print(frame)

    player1 = player.subsurface(
        (0, 0, player.get_width()/4, player.get_height()))

    # listen for key presses
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                background_loc = background_loc.move([scale, 0])
                for boundary in boundaries:
                    boundary = boundary.move_ip([scale, 0])
            if event.key in [K_d, K_RIGHT]:
                background_loc = background_loc.move([-scale, 0])
                for boundary in boundaries:
                    boundary = boundary.move_ip([-scale, 0])
            if event.key in [K_w, K_UP]:
                background_loc = background_loc.move([0, scale])
                for boundary in boundaries:
                    boundary = boundary.move_ip([0, scale])
            if event.key in [K_s, K_DOWN]:
                background_loc = background_loc.move([0, -scale])
                for boundary in boundaries:
                    boundary = boundary.move_ip([0, -scale])
            # print(boundaries)

    # test for collision
    print(player_hitbox.collidelist(boundaries))

  # draw graphics
  # pygame.draw.rect(
  #     screen,
  #     (50, 50, 50),
  #     (left, top, width, height)
  # )

  # draw map
    screen.blit(background, background_loc)
   # draw collisions
    for boundary in boundaries:
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            boundary
        )
    # draw player
    screen.blit(player, player_loc)
    pygame.draw.rect(screen,
                     (255, 0, 0),
                     player_hitbox)

    # update screen
    pygame.display.update()


pygame.quit()
