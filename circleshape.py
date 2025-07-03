import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y, radius):
        
        # If the subclass has a 'containers' attribute, register with the group
        if hasattr(self, "containers"):
            super().__init__(self.containers)  # Add to sprite groups specified in 'containers'
        else:
            super().__init__()  # Basic sprite init with no group

        self.position = pygame.Vector2(x, y)  # Position as a 2D vector
        self.velocity = pygame.Vector2(0, 0)  # Initial velocity is zero
        self.radius = radius  # Radius of the circle

    def draw(self,screen):
        pass  # Placeholder: To be overridden with custom draw logic

    def update(self,screen):
        pass  # Placeholder: To be overridden with movement/update logic

    def collides_with(self, other):
        # Collision check: returns True if the distance between two circles is less than or equal to the sum of their radii
        return self.position.distance_to(other.position) <= self.radius + other.radius

