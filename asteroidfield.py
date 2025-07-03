import pygame
import random
from asteroid import Asteroid
from constants import *

class AsteroidField(pygame.sprite.Sprite):
    # Define possible edges (directions and spawn positions) for asteroid spawning
    edges = [
        [  # Rightward-moving asteroid from left edge
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [  # Leftward-moving asteroid from right edge
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [  # Downward-moving asteroid from top edge
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [  # Upward-moving asteroid from bottom edge
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)  # Initialize as a pygame sprite
        self.spawn_timer = 0.0  # Timer to control spawn frequency

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)  # Create asteroid at given position and radius
        asteroid.velocity = velocity  # Assign initial velocity

    def update(self, dt):
        self.spawn_timer += dt  # Increase timer by delta time
        if self.spawn_timer > ASTEROID_SPAWN_RATE:  # Time to spawn a new asteroid
            self.spawn_timer = 0  # Reset timer

            # Choose a random edge to spawn from
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)  # Random speed
            velocity = edge[0] * speed  # Base direction vector scaled by speed
            velocity = velocity.rotate(random.randint(-30, 30))  # Add randomness to direction
            position = edge[1](random.uniform(0, 1))  # Get position along the edge
            kind = random.randint(1, ASTEROID_KINDS)  # Random size multiplier
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)  # Spawn asteroid
        
