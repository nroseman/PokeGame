# TODO: add collision detection  --done
# TODO: add stop for collision  --done
# TODO: make player class/refactor code/declutter main game loop -- in progress
# TODO: add map transitions for buildings/new map segments
# TODO: scale up images (without messing with Rects and movement) -- in progress

import pygame
from pygame.locals import *
from player import Player
import csv

frame = 1
scale = 16
mag = 2
tile_size = scale * mag
size = width, height = (20 * tile_size, 20 * tile_size)


pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PokeGame")

# set background color
screen.fill((20, 200, 50))


# apply changes
pygame.display.update()

# load images
background = pygame.image.load("./img/testMap.png").convert_alpha()
background = pygame.transform.scale(
    background, (background.get_width()*mag, background.get_height()*mag))
background_loc = background.get_rect()
# background_loc.center = width/2, height/2
player = pygame.image.load("./img/PlayerOD.png").convert_alpha()

# to get one slice of animation from image
# player1 = player.subsurface(0, 0, player.get_width()/4, player.get_height())

player = pygame.transform.scale(
    player, (player.get_width()*mag, player.get_height()*mag))
player_loc = player.get_rect(bottomleft=(width/2, height/2))
player_hitboxes = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
player_hitboxes['up'] = Rect(
    player_loc.left, player_loc.top, tile_size, tile_size)
player_hitboxes['down'] = Rect(
    player_loc.left, player_loc.top + (tile_size * 2), tile_size, tile_size)
player_hitboxes['left'] = Rect(
    player_loc.left - (tile_size), player_loc.top + (tile_size), tile_size, tile_size)
player_hitboxes['right'] = Rect(
    player_loc.left + (tile_size), player_loc.top + (tile_size), tile_size, tile_size)
player_hitbox = Rect(player_loc.left, player_loc.top +
                     scale, tile_size, tile_size)

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
            boundaries.append(
                Rect(j * tile_size, i * tile_size, tile_size, tile_size))


p1 = Player('image.png', width, height)
print(p1.position)

while running:
    screen.fill((20, 200, 50))

  # change frame rate
    # clock = pygame.time.Clock()
    # clock.tick(1)
    # print(frame)

    # player1 = player.subsurface(
    #     (0, 0, player.get_width()/4, player.get_height()))

  # listen for key presses
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                if (player_hitboxes['left'].collidelist(boundaries)) >= 0:
                    print(player_hitboxes['left'].collidelist(boundaries))
                    break
                else:
                    background_loc = background_loc.move([tile_size, 0])
                    for boundary in boundaries:
                        boundary = boundary.move_ip([tile_size, 0])

            if event.key in [K_d, K_RIGHT]:
                if (player_hitboxes['right'].collidelist(boundaries)) >= 0:
                    print(player_hitboxes['right'].collidelist(boundaries))
                    break
                else:
                    background_loc = background_loc.move([-tile_size, 0])
                    for boundary in boundaries:
                        boundary = boundary.move_ip([-tile_size, 0])
            if event.key in [K_w, K_UP]:
                if (player_hitboxes['up'].collidelist(boundaries)) >= 0:
                    print(player_hitboxes['up'].collidelist(boundaries))
                    break
                else:
                    background_loc = background_loc.move([0, tile_size])
                    for boundary in boundaries:
                        boundary = boundary.move_ip([0, tile_size])
            if event.key in [K_s, K_DOWN]:
                if (player_hitboxes['down'].collidelist(boundaries)) >= 0:
                    print(player_hitboxes['down'].collidelist(boundaries))
                    break
                else:
                    background_loc = background_loc.move([0, -tile_size])
                    for boundary in boundaries:
                        boundary = boundary.move_ip([0, -tile_size])

  # draw graphics
    # pygame.draw.rect(
    #     screen,
    #     (50, 50, 50),
    #     (left, top, width, height)
    # )

  # draw map
    screen.blit(background, background_loc)

  # draw collisions
    # for boundary in boundaries:
    #     pygame.draw.rect(
    #         screen,
    #         (255, 0, 0),
    #         boundary)

  # draw player
    screen.blit(player, player_loc)

  # draw player hitboxes
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitbox)
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitboxes['up'])
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitboxes['down'])
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitboxes['left'])
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitboxes['right'])

  # update screen
    pygame.display.update()


pygame.quit()
