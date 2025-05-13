from circleshape import *
from constants import *
from asteroidfield import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        a1_velocity = self.velocity.rotate(split_angle) * 1.2
        a2_velocity = self.velocity.rotate(-split_angle) * .8
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_velocity
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = a2_velocity

        
