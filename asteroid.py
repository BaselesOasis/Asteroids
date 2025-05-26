from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            rotation = random.uniform(20, 50)
            velocity_asteroid1 = self.velocity.rotate(rotation)
            velocity_asteroid2 = self.velocity.rotate(-rotation)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity_asteroid1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = velocity_asteroid2
            self.kill()
            return new_asteroid1, new_asteroid2



    def update(self, dt):
        self.position += self.velocity * dt

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)