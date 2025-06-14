import pygame
from constants import *
from circleshape import *
import random
import math

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)
        self.lumpy_shape = self.generate_lumpy_shape()
    def generate_lumpy_shape(self):
        points = []
        num_points = random.randint(10, 16)
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i
            # Perturb radius slightly for lumpiness
            offset = random.uniform(0.8, 1.2)
            r = self.radius * offset
            x = self.position.x + r * math.cos(angle)
            y = self.position.y + r * math.sin(angle)
            points.append((x, y))
        return points
    
    def draw(self, screen):
    
        pygame.draw.polygon(screen, "white", self.lumpy_shape, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # Wrap around screen edges
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH

        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

    # Move each point of the lumpy shape accordingly
        dx = self.velocity.x * dt
        dy = self.velocity.y * dt
        
        self.lumpy_shape = [(x + dx, y + dy) for (x, y) in self.lumpy_shape]

    # Re-center shape if wrapping occurred
        if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH or self.position.y <= 0 or self.position.y >= SCREEN_HEIGHT:
            self.lumpy_shape = self.generate_lumpy_shape()

    def split(self):

        self.kill()

        if(self.radius<ASTEROID_MIN_RADIUS+3):
                return
        
        random_angle = random.uniform(20,50)
        a=self.velocity.rotate(random_angle)                
        b=self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity = a * 1.2

        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2.velocity = b * 1.2
