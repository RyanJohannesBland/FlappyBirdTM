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

        self.base_image = pygame.image.load("images/pipe.png").convert_alpha()

        y_position = random.choice([self.pipe_height, SCREEN_HEIGHT + 20])
        self.position = Vector((SCREEN_WIDTH + PIPE_WIDTH, y_position))

        if y_position == self.pipe_height:
            self.surface = pygame.transform.rotate(self.base_image, 180)
        else:
            self.surface = self.base_image
        self.rect = self.surface.get_rect()

        self.rect.midbottom = self.position

    def move(self):
        self.position.x -= self.board_reference.game_speed
        if self.position.x < -PIPE_WIDTH:
            self.kill()
        self.rect.midbottom = self.position

    def detect_collision(self, rect):
        if self.rect.colliderect(rect):
            self.surface.fill((40, 255, 255))
