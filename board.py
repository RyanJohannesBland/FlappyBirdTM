import sys
import pygame
from pygame.constants import *
from physics_constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from bird import Bird
from pipe import Pipe


class Board():
    def __init__(self):
        self.game_speed = 1
        self.internal_timer = 0
        self.actions = dict()

        pygame.init()
        pygame.display.set_caption("Flappy Bird")

        self.clock = pygame.time.Clock()
        self.displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.background = pygame.image.load("images/background.jpg").convert_alpha()

        self.pipes = pygame.sprite.Group()
        self.bird = Bird()

    def add_action(self, time_interval, function):
        self.actions.setdefault(time_interval, list())
        if function == "spawn_pipe":
            self.actions[time_interval].append(self.spawn_pipe)
        elif function == "increase_game_speed":
            self.actions[time_interval].append(self.increase_game_speed)

    def _trigger_self_actions(self):
        for time_interval, actions in self.actions.items():
            if self.internal_timer % time_interval == 0:
                for action in actions:
                    action()

    def spawn_pipe(self):
        self.pipes.add(Pipe(self))

    def increase_game_speed(self):
        self.game_speed += 1

    def _tick(self):
        self.internal_timer += 1
        self._trigger_self_actions()

    def _redraw(self):
        self.displaysurface.blit(self.background, (0, 0))

        self.displaysurface.blit(self.bird.surface, self.bird.rect)
        for pipe in self.pipes:
            pipe.detect_collision(self.bird.rect)
            self.displaysurface.blit(pipe.surface, pipe.rect)

        pygame.display.update()

    def start_game_loop(self):
        while True:
            # Handle quitting the game.
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.end_game_loop()

            self._tick()
            self._redraw()

            self.clock.tick(FPS)

            self.bird.move()
            for entity in self.pipes:
                entity.move()

    def end_game_loop(self):
        pygame.quit()
        sys.exit()