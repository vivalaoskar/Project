import pygame
import random

class MatrixLetters:
    def __init__(self, app):
        self.app = app
        self.letters = [chr(int('0x30a0', 16) + i) for i in range(1, 95)]
        self.font_size = 10
        self.font = pygame.font.Font('MS Mincho.ttf', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0,100,0))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render, pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()


class MatrixApp:
    def __init__(self):
        self.RES = self.WIDTH, self.HEIGHT = 1400, 800

        pygame.init()
        self.screen = pygame.display.set_mode(self.RES)
        self.surface = pygame.Surface(self.RES, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.matrixLetters = MatrixLetters(self)

    def draw(self):
        self.surface.fill((0,0,0,10))
        self.matrixLetters.run()
        self.screen.blit(self.surface, (0,0))

    def run(self):
        while True:
            self.draw()
            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.flip()
            self.clock.tick(50)

if __name__ == '__main__':
    app = MatrixApp()
    app.run()
