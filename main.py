# TODO: add collision detection  --done
# TODO: add stop for collision  --done
# TODO: make player class/refactor code -- in progress
# TODO: make map class/refactor code -- in progress
# TODO: scale up images (without messing with Rects and movement) -- partial (collisions don't scale with screen size)
# TODO: add offset for player spawn -- done
# TODO: add player walk animation  -- line 137 and player.py -- done
# TODO: add map transitions for buildings/new map segments
# TODO: make player move entire time key is pressed -- done


import sys
import pygame
import csv
from pygame.locals import *
from player import Player
from map import Map

pygame.init()

frame = 1
scale = 16
mag = 3
tile_size = scale * mag
size = screen_width, screen_height = (20 * tile_size, 20 * tile_size)
hold_frames = 1
fps = 30

level = Map(mag, screen_width, screen_height, tile_size)
p1 = Player(screen_width, screen_height, fps)

velocity = 1

move_direction = {
    'up': pygame.Vector2(0, velocity),
    'down': pygame.Vector2(0, -velocity),
    'left': pygame.Vector2(velocity, 0),
    'right': pygame.Vector2(-velocity, 0),
    'none': pygame.Vector2(0, 0)
}


dx = 0
destination = 0


running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PokeGame")

# set background color
screen.fill((20, 200, 50))

# load images
background = pygame.image.load("./img/testMap.png").convert_alpha()
background = pygame.transform.scale(
    background, (background.get_width()*mag, background.get_height()*mag))
background_loc = background.get_rect(topleft=(level.offset))
# background_loc.center = screen_width/2, screen_height/2
player = pygame.image.load("./img/PlayerDown_1.png").convert_alpha()

# to get one slice of animation from image
# player1 = player.subsurface(0, 0, player.get_width()/4, player.get_height())

# player = pygame.transform.scale(
#     player, (player.get_width()*mag, player.get_height()*mag))
# player_loc = player.get_rect(bottomleft=(screen_height/2, screen_width/2))
player_hitboxes = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
player_hitboxes['up'] = Rect(
    p1.position.left, p1.position.top, tile_size, tile_size)
player_hitboxes['down'] = Rect(
    p1.position.left, p1.position.top + (tile_size * 2), tile_size, tile_size)
player_hitboxes['left'] = Rect(
    p1.position.left - (tile_size), p1.position.top + (tile_size), tile_size, tile_size)
player_hitboxes['right'] = Rect(
    p1.position.left + (tile_size), p1.position.top + (tile_size), tile_size, tile_size)
player_hitbox = Rect(p1.position.left, p1.position.top +
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

# initial load
screen.blit(background, background_loc)
p1.draw(mag, screen)
pygame.display.update()
print(dx < destination)
# MAIN GAME LOOP
while running:
    # screen.fill((20, 200, 50))

    #   change frame rate
    clock = pygame.time.Clock()
    clock.tick(fps)

# reset variables
    destination = 0
    dx = 0
    p1.reset()
    screen.fill((20, 200, 50))
    screen.blit(background, background_loc)
    p1.draw(mag, screen)
    pygame.display.update()
    # player1 = player.subsurface(
    #     (0, 0, player.get_width()/4, player.get_height()))

  # listen for exit
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

  # listen for direction keys
    if not destination:
        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            if (player_hitboxes['left'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['left'].collidelist(boundaries))
                p1.walking = False
            else:
                p1.walking = True
            p1.direction = 1
            p1.animate = True
            p1.moving = p1.is_moving()
            if p1.moving:
                destination = tile_size
            print(p1.moving)

            # walking animation loop
            while dx < destination:
                background_loc = background_loc.move(
                    (move_direction['left']*p1.moving))
                for boundary in boundaries:
                    boundary = boundary.move_ip(
                        (move_direction['left']*p1.moving))
                # set correct image for animation
                p1.update(dx, tile_size)
                # draw background
                screen.blit(background, background_loc)
                # draw player
                p1.draw(mag, screen)
                pygame.display.update()
                dx += velocity

        elif keys[K_s] or keys[K_DOWN]:
            if (player_hitboxes['down'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['down'].collidelist(boundaries))
                p1.walking = False
            else:
                p1.walking = True
            p1.direction = 0
            p1.animate = True
            p1.moving = p1.is_moving()
            if p1.moving:
                destination = tile_size
            print(p1.moving)

            # walking animation loop
            while dx < destination:
                background_loc = background_loc.move(
                    (move_direction['down']*p1.moving))
                for boundary in boundaries:
                    boundary = boundary.move_ip(
                        (move_direction['down']*p1.moving))
                # set correct image for animation
                p1.update(dx, tile_size)
                # draw background
                screen.blit(background, background_loc)
                # draw player
                p1.draw(mag, screen)
                pygame.display.update()
                dx += velocity

        elif keys[K_d] or keys[K_RIGHT]:
            if (player_hitboxes['right'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['right'].collidelist(boundaries))
                p1.walking = False
            else:
                p1.walking = True
            p1.direction = 2
            p1.animate = True
            p1.moving = p1.is_moving()
            if p1.moving:
                destination = tile_size
            print(p1.moving)

            # walking animation loop
            while dx < destination:
                background_loc = background_loc.move(
                    (move_direction['right']*p1.moving))
                for boundary in boundaries:
                    boundary = boundary.move_ip(
                        (move_direction['right']*p1.moving))
                # set correct image for animation
                p1.update(dx, tile_size)
                # draw background
                screen.blit(background, background_loc)
                # draw player
                p1.draw(mag, screen)
                pygame.display.update()
                dx += velocity

        elif keys[K_w] or keys[K_UP]:
            if (player_hitboxes['up'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['up'].collidelist(boundaries))
                p1.walking = False
            else:
                p1.walking = True
            p1.direction = 3
            p1.animate = True
            p1.moving = p1.is_moving()
            if p1.moving:
                destination = tile_size
            print(p1.moving)

            # walking animation loop
            while dx < destination:
                background_loc = background_loc.move(
                    (move_direction['up']*p1.moving))
                for boundary in boundaries:
                    boundary = boundary.move_ip(
                        (move_direction['up']*p1.moving))
                # set correct image for animation
                p1.update(dx, tile_size)
                # draw background
                screen.blit(background, background_loc)
                # draw player
                p1.draw(mag, screen)
                pygame.display.update()
                dx += velocity

            # background_loc = background_loc.move(velocity['down'])
            # for boundary in boundaries:
            #     boundary = boundary.move_ip(velocity['down'])
    # background.draw
  # draw map
    # if p1.walking:
    #     background_loc = background_loc.move(velocity[p1.direction])
    # screen.blit(background, background_loc)
    # p1.update(hold_frames)
    # p1.draw(mag, screen)

    # boundaries.draw
    # p1.update

  # draw graphics
    # pygame.draw.rect(
    #     screen,
    #     (50, 50, 50),
    #     (left, top, screen_width, screen_height)
    # )

  # draw collisions
    for boundary in boundaries:
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            boundary)

  # draw player
    # screen.blit(player, player_loc)

#   draw player hitboxes
    # pygame.draw.rect(screen,
    #                  (255, 0, 255),
    #                  player_hitboxes['up'])
    # pygame.draw.rect(screen,
    #                  (255, 255, 0),
    #                  player_hitboxes['down'])
    # pygame.draw.rect(screen,
    #                  (255, 0, 0),
    #                  player_hitboxes['left'])
    # pygame.draw.rect(screen,
    #                  (0, 255, 255),
    #                  player_hitboxes['right'])

  # update screen
    pygame.display.update()


pygame.quit()
