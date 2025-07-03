import pygame
from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)  # Initialize CircleShape with position and player radius
        self.rotation = 0  # Angle of the player's facing direction (degrees)
        self.shoot_timer=0  # Time until the player can shoot again

    def draw(self,screen):
        # Draw the player as a white triangle
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def triangle(self):
        # Calculate the three points of a triangle based on rotation and radius
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Direction player is facing
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5  # Perpendicular vector for width

        # Point of triangle (tip) and two base points
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right            
        c = self.position - forward * self.radius + right

        return [a, b, c]  # Return list of triangle vertices

    def rotate(self, dt):
        # Rotate the player by TURN_SPEED scaled by delta time
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_timer -= dt  # Decrease shoot cooldown timer
        keys = pygame.key.get_pressed()  # Get current key state

        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left

        if keys[pygame.K_d]:
            self.rotate(dt)  # Rotate right

        # Move forward or backward
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward

        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward

        # Fire a shot if space is pressed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        # Move the player forward in the direction they are facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Only shoot if cooldown has elapsed
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown
        
        # Create a new shot object at player's position
        shot = Shot(self.position.x, self.position.y)
        # Set shot velocity in the direction of player rotation
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

