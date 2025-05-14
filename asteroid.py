from random import uniform

import pygame

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = uniform(20,50)
        first_child_velocity = self.velocity.rotate(angle)
        second_child_velocity = self.velocity.rotate(-angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        first_child = Asteroid(
            self.position.x,
            self.position.y, 
            child_radius
        )
        first_child.velocity = first_child_velocity * 1.2
        second_child = Asteroid(
            self.position.x,
            self.position.y,
            child_radius,
        )
        second_child.velocity = second_child_velocity * 1.2

        