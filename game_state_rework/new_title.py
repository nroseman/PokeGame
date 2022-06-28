import pygame

from walking import Walking


class Title:
    def __init__(self, game):
        self.game = game
        self.canvas = pygame.Surface((256, 192))

    def update(self):
        self.event_handler()

    def event_handler(self):
        if self.game.key_pressed['escape']:
            print("handled")
            new_state = Walking(self.game)
            self.game.state_stack.append(new_state)

    def render(self):
        font_type = pygame.font.Font('../font/PressStart2P-Regular.ttf', 20)
        text = font_type.render("Press Start", False, (0, 0, 0))
        display = pygame.image.load(
            '../img/map/rockMap80_80.png').convert_alpha()
        position = (0, 0)

        self.canvas.blit(display, position)
        self.canvas.blit(text, ((self.canvas.get_width() / 2) -
                         (text.get_width() / 2), (self.canvas.get_height() / 2) -
                         (text.get_height() / 2)))

        return self.canvas
