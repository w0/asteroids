import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vel_negative = self.velocity.rotate(-angle)
        vel_positive = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_negative * ASTEROID_SPLIT_SPEED
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_positive * ASTEROID_SPLIT_SPEED


    def update(self, dt):
        self.position += self.velocity * dt
