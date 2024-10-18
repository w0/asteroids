import pygame

class Score():
    def __init__(self, font_size=36):
        self.player_score = 0
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen, position=(10, 10), color=(255, 255, 255)):
        text_surface = self.font.render(f"score: {self.player_score}", True, color)
        screen.blit(text_surface, position)

    def update(self, points: int):
        self.player_score += points
