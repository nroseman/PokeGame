import pygame
from new_map import Map
from new_player import Player


class Walking:
    def __init__(self, game):
        self.game = game
        self.canvas = pygame.Surface((256, 192))
        self.portal_loc = (100, 100)
        self.map = Map()
        self.player = Player(self.canvas)
        self.direction = pygame.Vector2()
        self.prev_direction = 0

    def update(self):
        self.event_handler()
        self.map.update(self.direction, self.player.moving)
        # player.update()
        self.reset()

    def event_handler(self):
        # Check if in Animation Loop
        if self.player.animate:
            pass
        else:
            # Check if Direction Key Pressed
            if self.game.key_dir and not self.game.key_pressed['escape']:
                print(self.game.key_dir)
                # Check for Collisions
                if self.player.hitboxes[self.game.key_dir].collidelist(self.map.boundaries) < 0:
                    print(self.player.hitboxes[self.game.key_dir].collidelist(
                        self.map.boundaries))
                    self.player.moving = True
                # Set Movement Vector
                self.direction = pygame.Vector2(
                    self.game.key_pressed['left'] -
                    self.game.key_pressed['right'],
                    self.game.key_pressed['up'] - self.game.key_pressed['down'])
                # TODO: Start Here

    def render(self):
        # Get Map Surface and Position
        map_info = self.map.render()
        # Draw Map onto Canvas
        self.canvas.blit(map_info[0], map_info[1])
        # drawing boundary for testing
        for boundary in self.map.boundaries:
            pygame.draw.rect(
                self.canvas,
                (255, 0, 0),
                boundary)
        # drawing hitboxes for testing
        for hitbox in self.player.hitboxes.values():
            pygame.draw.rect(
                self.canvas,
                (255, 0, 0),
                hitbox)

        # TODO: Add player.render()
        player_info = self.player.render()
        # Draw Player onto Canvas
        self.canvas.blit(player_info[0], player_info[1])
        # Return Finished Canvas
        return self.canvas

    def reset(self):
        self.prev_direction = self.direction
        # self.direction = pygame.Vector2()
        self.player.moving = False
