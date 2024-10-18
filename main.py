import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = Score(font_size=48)

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)

        for object in asteroids:
            if object.collision(player):
                player.death(screen)
                if player.lives < 0:
                    print("Game over!")
                    sys.exit(0)

            for bullet in shots:
                if object.collision(bullet):
                    bullet.kill()
                    score.update(object.split())

        screen.fill("black")

        for object in drawable:
            object.draw(screen)
            score.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
