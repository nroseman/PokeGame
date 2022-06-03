# TODO: add collision detection  --done
# TODO: add stop for collision  --done
# TODO: make player class/refactor code -- in progress
# TODO: make map class/refactor code -- in progress
# TODO: scale up images (without messing with Rects and movement) -- partial (collisions don't scale with screen size)
# TODO: add offset for player spawn -- done
# TODO: add player walk animation  -- line 137 and player.py (need to alternate images for animation)
# TODO: add map transitions for buildings/new map segments
# TODO: make player move entire time key is pressed


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

velocity = {
    'up': pygame.Vector2(0, float(tile_size/fps)),
    'down': pygame.Vector2(0, float(-tile_size/fps)),
    'left': pygame.Vector2(tile_size/fps, 0),
    'right': pygame.Vector2(-tile_size/fps, 0),
    'none': pygame.Vector2(0, 0)
}


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
player = pygame.image.load("./img/PlayerDown_1.png").convert_alpha()

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


# MAIN GAME LOOP
while running:
    screen.fill((20, 200, 50))

#   change frame rate
    clock = pygame.time.Clock()
    clock.tick(fps)

# check for hold frames for animations
    if hold_frames > 1:
        accept_input = False
        hold_frames -= 1
    else:
        accept_input = True
        hold_frames = 1
        p1.reset()

    # player1 = player.subsurface(
    #     (0, 0, player.get_width()/4, player.get_height()))

  # listen for exit
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

  # listen for direction keys
    if accept_input:
        keys = pygame.key.get_pressed()
        if keys[K_a] or keys[K_LEFT]:
            if (player_hitboxes['left'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['left'].collidelist(boundaries))
                p1.walking = False
                break
            else:
                animation_frame = 0
                while animation_frame < fps:
                    hold_frames = 1
                    background_loc = background_loc.move(velocity['left'])
                    for boundary in boundaries:
                        boundary = boundary.move_ip(velocity['left'])
                        p1.update(animation_frame)
                    p1.draw(mag, screen)
                    pygame.display.update()
                    animation_frame += 1

        elif keys[K_s] or keys[K_DOWN]:
            if (player_hitboxes['down'].collidelist(boundaries)) >= 0:
                print(player_hitboxes['down'].collidelist(boundaries))
                p1.walking = False
            else:
                p1.walking = True
                p1.animate = True
                # hold_frames = fps - 1
                animation_frame = 0
                while animation_frame < fps:
                    hold_frames = 1
                    background_loc = background_loc.move(velocity['down'])
                    for boundary in boundaries:
                        boundary = boundary.move_ip(velocity['down'])
                        p1.update(animation_frame)
                    screen.blit(background, background_loc)
                    p1.draw(mag, screen)
                    pygame.display.update()
                    animation_frame += 1

            # background_loc = background_loc.move(velocity['down'])
            # for boundary in boundaries:
            #     boundary = boundary.move_ip(velocity['down'])
    # background.draw
  # draw map
    if p1.walking:
        background_loc = background_loc.move(velocity[p1.direction])
    screen.blit(background, background_loc)
    p1.update(hold_frames)
    p1.draw(mag, screen)

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
