import pygame

from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.invulnerability = 0
        self.rotation = 0
        self.shot_timer = 0
        self.sound_death = pygame.mixer.Sound("./assets/death.wav")
        self.sound_shoot = pygame.mixer.Sound("./assets/shoot.wav")
        self.lives = 3

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())

    def death(self, screen):
        if self.invulnerability > 0:
            return

        pygame.mixer.Sound.play(self.sound_death)
        self.invulnerability = PLAYER_INVULNERABILITY
        self.lives -= 1
        self.draw(screen)
        print(f"Remain: {self.lives}")

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def shoot(self):
        if self.shot_timer > 0:
            return

        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        pygame.mixer.Sound.play(self.sound_shoot)
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_velocity = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity = shot_velocity * PLAYER_SHOOT_SPEED

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        if self.shot_timer > 0:
            self.shot_timer -= dt

        if self.invulnerability > 0:
            self.invulnerability -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot( )
