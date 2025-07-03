import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self,x,y):
        # Initialize the shot as a circle at (x, y) with a fixed radius
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self,screen):
        # Draw the shot as a white outlined circle
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        # Move the shot according to its velocity and the time elapsed
        self.position += self.velocity * dt

