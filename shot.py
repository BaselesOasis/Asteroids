from circleshape import CircleShape
from constants import * 
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius, position, velocity):
        super().__init__(x, y, radius)
        self.position = position
        self.velocity = velocity
    

    def update(self, dt):
        self.position += self.velocity * dt

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)