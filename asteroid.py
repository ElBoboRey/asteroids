from circleshape import*
import pygame
from constants import*
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        old_velocity = self.velocity.copy()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
            new_asteroid_1.velocity = old_velocity.rotate(random_angle) * 1.2
            
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, (old_radius - ASTEROID_MIN_RADIUS))
            new_asteroid_2.velocity = old_velocity.rotate(random_angle * -1) * 1.2