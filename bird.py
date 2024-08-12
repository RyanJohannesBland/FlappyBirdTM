import pygame
from pygame.locals import K_SPACE
from pygame.math import Vector2 as Vector
from physics_constants import SCREEN_HEIGHT, TERMINAL_VELOCITY, GRAVITY, JUMP_COOLDOWN, JUMP_HEIGHT


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("images/bird.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.spawn()

    def spawn(self):
        self.is_alive = True
        self.position = Vector((50, 385))
        self.velocity = Vector(0,0)
        self.jump_cooldown = 0

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_SPACE]:
            self.jump()

        self.fall()

        self.position += self.velocity

        self.position.y = max(0, self.position.y)
        self.position.y = min(SCREEN_HEIGHT, self.position.y)

        self.rect.midbottom = self.position

        self.jump_cooldown = max(0, self.jump_cooldown - 1)

    def jump(self):
        if not self.jump_cooldown:
            self.velocity.y = -JUMP_HEIGHT
            self.jump_cooldown = JUMP_COOLDOWN

    def fall(self):
        self.velocity.y = min(TERMINAL_VELOCITY, self.velocity.y + GRAVITY)
