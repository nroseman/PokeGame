# TODO: add collision detection  --done
# TODO: add stop for collision  --done
# TODO: make player class/refactor code -- in progress
# TODO: make map class/refactor code -- in progress
# TODO: scale up images (without messing with Rects and movement) -- partial (collisions don't scale with screen size)
# TODO: add offset for player spawn -- done
# TODO: add player walk animation  -- line 137 and player.py (need to alternate images for animation)
# TODO: add map transitions for buildings/new map segments
# TODO: make player move entire time key is pressed


import pygame
import csv
from pygame.locals import *
from player import Player
from map import Map

frame = 1
scale = 16
mag = 3
tile_size = scale * mag
size = screen_width, screen_height = (20 * tile_size, 20 * tile_size)

level = Map(mag, screen_width, screen_height, tile_size)
character = Player(mag, screen_width, screen_height)


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
background_loc = background.get_rect(topleft=(level.offset))
# background_loc.center = screen_width/2, screen_height/2
player = pygame.image.load("./img/PlayerOD.png").convert_alpha()

# to get one slice of animation from image
# player1 = player.subsurface(0, 0, player.get_width()/4, player.get_height())

player = pygame.transform.scale(
    player, (player.get_width()*mag, player.get_height()*mag))
player_loc = player.get_rect(bottomleft=(screen_height/2, screen_width/2))
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
                Rect(j * tile_size - (level.offset[1]), i * tile_size - (level.offset[0]), tile_size, tile_size))


p1 = Player('image.png', screen_width, screen_height)
print(p1.position)
print(background_loc)

while running:
    screen.fill((20, 200, 50))

#   change frame rate
    clock = pygame.time.Clock()
    clock.tick(2)
    print(frame)

  # draw map
    screen.blit(background, background_loc)

    # player1 = player.subsurface(
    #     (0, 0, player.get_width()/4, player.get_height()))

  # listen for key presses
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # if event.type == KEYDOWN:
        #     if event.key in [K_a, K_LEFT]:
        #         if (player_hitboxes['left'].collidelist(boundaries)) >= 0:
        #             print(player_hitboxes['left'].collidelist(boundaries))
        #             break
        #         else:
        #             background_loc = background_loc.move([tile_size, 0])
        #             for boundary in boundaries:
        #                 boundary = boundary.move_ip([tile_size, 0])

        #     if event.key in [K_d, K_RIGHT]:
        #         if (player_hitboxes['right'].collidelist(boundaries)) >= 0:
        #             print(player_hitboxes['right'].collidelist(boundaries))
        #             break
        #         else:
        #             background_loc = background_loc.move([-tile_size, 0])
        #             for boundary in boundaries:
        #                 boundary = boundary.move_ip([-tile_size, 0])
        #     if event.key in [K_w, K_UP]:
        #         if (player_hitboxes['up'].collidelist(boundaries)) >= 0:
        #             print(player_hitboxes['up'].collidelist(boundaries))
        #             break
        #         else:
        #             background_loc = background_loc.move([0, tile_size])
        #             for boundary in boundaries:
        #                 boundary = boundary.move_ip([0, tile_size])
        #     if event.key in [K_s, K_DOWN]:
        #         if (player_hitboxes['down'].collidelist(boundaries)) >= 0:
        #             print(player_hitboxes['down'].collidelist(boundaries))
        #             break
        #         else:
        #             background_loc = background_loc.move([0, -tile_size])
        #             for boundary in boundaries:
        #                 boundary = boundary.move_ip([0, -tile_size])
    keys = pygame.key.get_pressed()
    if keys[K_a] or keys[K_LEFT]:
        if (player_hitboxes['left'].collidelist(boundaries)) >= 0:
            print(player_hitboxes['left'].collidelist(boundaries))
            break
        else:

            background_loc = background_loc.move([tile_size, 0])
            for boundary in boundaries:
                boundary = boundary.move_ip([tile_size, 0])

    # if keys[K_d, K_RIGHT]:
    #     if (player_hitboxes['right'].collidelist(boundaries)) >= 0:
    #         print(player_hitboxes['right'].collidelist(boundaries))
    #         break
    #     else:
    #         background_loc = background_loc.move([-tile_size, 0])
    #         for boundary in boundaries:
    #             boundary = boundary.move_ip([-tile_size, 0])
    # if keys[K_w, K_UP]:
    #     if (player_hitboxes['up'].collidelist(boundaries)) >= 0:
    #         print(player_hitboxes['up'].collidelist(boundaries))
    #         break
    #     else:
    #         background_loc = background_loc.move([0, tile_size])
    #         for boundary in boundaries:
    #             boundary = boundary.move_ip([0, tile_size])
    if keys[K_s] or keys[K_DOWN]:
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
    #     (left, top, screen_width, screen_height)
    # )

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
