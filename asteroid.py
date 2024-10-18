import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.kill_sound = pygame.mixer.Sound("./assets/break.wav")

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self) -> int:
        self.kill()
        pygame.mixer.Sound.play(self.kill_sound)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return 20

        angle = random.uniform(20, 50)
        vel_negative = self.velocity.rotate(-angle)
        vel_positive = self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_negative * ASTEROID_SPLIT_SPEED
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vel_positive * ASTEROID_SPLIT_SPEED

        if self.radius == 60:
            return 60

        if self.radius == 40:
            return 40

        return 0

    def update(self, dt):
        self.position += self.velocity * dt
