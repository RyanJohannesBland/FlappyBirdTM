import random
import pygame
from pygame.math import Vector2 as Vector
from physics_constants import SCREEN_WIDTH, SCREEN_HEIGHT


PIPE_WIDTH = 20

class Pipe(pygame.sprite.Sprite):
    def __init__(self, board_reference):
        super().__init__()
        self.board_reference = board_reference
        self.pipe_height = random.randint(50, 250)

        self.surface = pygame.Surface((PIPE_WIDTH, self.pipe_height))
        self.surface.fill((255,255,40))
        self.rect = self.surface.get_rect()

        x = random.choice([self.pipe_height, SCREEN_HEIGHT])
        self.position = Vector((SCREEN_WIDTH + PIPE_WIDTH, x))
        self.rect.midbottom = self.position

    def move(self):
        self.position.x -= self.board_reference.game_speed
        if self.position.x < -PIPE_WIDTH:
            self.kill()
        self.rect.midbottom = self.position

    def detect_collision(self, rect):
        if self.rect.colliderect(rect):
            self.surface.fill((40, 255, 255))
