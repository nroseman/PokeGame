import sys
import pygame
from new_title import Title
from pygame.locals import *

# Adding Game class


class Game:
    def __init__(self):
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1024, 768
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 10
        self.clock = pygame.time.Clock()
        self.running = True
        self.state_stack = []
        self.key_pressed = {'left': False, 'right': False,
                            'down': False, 'up': False, 'escape': False}
        self.key_dir = 0
        self.start()

    def game_loop(self):
        # Lower FPS
        self.clock.tick(self.FPS)
        # Get Key Press
        self.get_events()
        # Call Update Method on Current Game State
        self.update()
        # Call Render Method on Current Game State
        self.render()
        # Reset Stuff
        self.reset()

    def start(self):
        # Load Title Menu
        self.screen.fill((0, 0, 0))
        self.title_menu = Title(self)
        self.state_stack.append(self.title_menu)

    def get_events(self):
        # Always Have Option to Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
        # Set Button Press
        self.keys = pygame.key.get_pressed()
        if self.keys[K_ESCAPE]:
            self.key_pressed['escape'] = True
        elif self.keys[K_a] or self.keys[K_LEFT]:
            self.key_pressed['left'] = True
            self.key_dir = 'left'
        elif self.keys[K_d] or self.keys[K_RIGHT]:
            self.key_pressed['right'] = True
            self.key_dir = 'right'
        elif self.keys[K_s] or self.keys[K_DOWN]:
            self.key_pressed['down'] = True
            self.key_dir = 'down'
        elif self.keys[K_w] or self.keys[K_UP]:
            self.key_pressed['up'] = True
            self.key_dir = 'up'

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        canvas_info = self.state_stack[-1].render()
        self.screen.blit(pygame.transform.scale(
            canvas_info, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0, 0))
        pygame.display.update()

    def reset(self):
        for key in self.key_pressed:
            self.key_pressed[key] = False
        self.screen.fill((0, 0, 0))
        self.key_dir = 0


# Main Game Loop
if __name__ == "__main__":
    game = Game()
    while game.running == True:
        game.game_loop()
    pygame.quit()
    sys.exit()
