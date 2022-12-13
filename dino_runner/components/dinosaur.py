import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING
JUMPING_ACTION = "jumping"
RUNNING_ACTION = "running"

class Dinosaur(Sprite):
    Y_POS = 310
    X_POS = 80
    YUMP_VELOCITY = 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.jump_velocity = self.YUMP_VELOCITY
        self.step = 0
        self.action = RUNNING_ACTION

    def update(self, user_input):
        if self.action == RUNNING_ACTION:
            self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
            self.step += 1
        elif self.action == JUMPING_ACTION:
            self.image = JUMPING_ACTION
            self.rect.y -= self.jump_velocity * 4
            self.jump_velocity -= 0.8

            if self.jump_velocity < -self.YUMP_VELOCITY:
                self.rect.y = self.Y_POS
                self.jump_velocity = self.YUMP_VELOCITY
                self.action = RUNNING_ACTION

        if user_input[pygame.K_UP] and self.action != JUMPING_ACTION:
            self.action = JUMPING_ACTION
        elif self.action != JUMPING_ACTION:
            self.action = RUNNING_ACTION

        if self.step >= 9:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
