import pygame
from constants import *
from circleshape import *
import math
import random

class Asteroid(CircleShape):
    
    def __init__(self,x,y,radius):
        super().__init__(x, y, radius)  # Initialize base CircleShape with position and radius
        self.lumpy_shape = self.generate_lumpy_shape()  # Generate the asteroid's jagged outer shape

    def generate_lumpy_shape(self):
        points = []
        num_points = random.randint(10, 16)  # Number of points to define the lumpy shape
        for i in range(num_points):
            angle = (2 * math.pi / num_points) * i  # Angle around the circle
            offset = random.uniform(0.8, 1.2)  # Random multiplier to create lumpiness
            r = self.radius * offset  # Adjusted radius
            x = self.position.x + r * math.cos(angle)  # Compute x-coordinate
            y = self.position.y + r * math.sin(angle)  # Compute y-coordinate
            points.append((x, y))  # Add point to shape
        return points  # Return list of shape points
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (49,70,154), self.lumpy_shape, 2)  # Draw lumpy shape outline

    def update(self, dt):
        self.position += self.velocity * dt  # Move asteroid by velocity scaled by delta time

        # Wrap around screen horizontally
        if self.position.x < 0:
            self.position.x += SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x -= SCREEN_WIDTH

        # Wrap around screen vertically
        if self.position.y < 0:
            self.position.y += SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y -= SCREEN_HEIGHT

        # Move each vertex of the lumpy shape according to the velocity
        dx = self.velocity.x * dt
        dy = self.velocity.y * dt
        self.lumpy_shape = [(x + dx, y + dy) for (x, y) in self.lumpy_shape]

        # If position has wrapped, regenerate the shape to re-center it around new position
        if self.position.x <= 0 or self.position.x >= SCREEN_WIDTH or self.position.y <= 0 or self.position.y >= SCREEN_HEIGHT:
            self.lumpy_shape = self.generate_lumpy_shape()

    def split(self):
        self.kill()  # Remove current asteroid

        # Don't split if too small
        if(self.radius<ASTEROID_MIN_RADIUS+3):
                return
        
        random_angle = random.uniform(20,50)  # Random angle to diverge new asteroids
        a=self.velocity.rotate(random_angle)  # First split direction
        b=self.velocity.rotate(-random_angle)  # Second split direction

        new_radius = self.radius - ASTEROID_MIN_RADIUS  # Reduce size for new asteroids

        # Create first split asteroid with rotated velocity
        asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid1.velocity = a * 1.2  # Slightly faster

        # Create second split asteroid with opposite rotated velocity
        asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
        asteroid2.velocity = b * 1.2  # Slightly faster

