import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()  # Initialize all imported pygame modules
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  # Create the game window
    
    #create a clock to manage framerate
    clock=pygame.time.Clock()
    #set a delta time variable
    dt=0  # Delta time between frames, used for time-based movement
    
    # Sprite groups for updating and drawing
    updatable = pygame.sprite.Group()  # Sprites with update logic
    drawable = pygame.sprite.Group()  # Sprites that need to be drawn

    # Assign containers (sprite groups) to AsteroidField so new asteroids go into them
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()  # Create the field manager for spawning asteroids
    
    asteroids = pygame.sprite.Group()  # Track all active asteroids
    shots = pygame.sprite.Group()  # Track all active shots

    # Assign appropriate sprite groups to each sprite class
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    
    # Create the player at the center of the screen
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    running = True  # Main game loop flag

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit if the window is closed
                return
    
        updatable.update(dt)  # Call update(dt) on all updatable sprites
        
        # Collision checks
        for asteroid in asteroids:
            if asteroid.collides_with(player):  # Asteroid hits player
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):  # Shot hits asteroid
                    shot.kill()  # Remove the shot
                    asteroid.split()  # Break the asteroid into smaller pieces

        screen.fill((0,0,0))  # Clear the screen with black background
        
        for obj in drawable:
            obj.draw(screen)  # Draw each drawable object

        pygame.display.flip()  # Swap the back buffer to the screen

        #limit framerate to 60 fps
        dt=clock.tick(60)/1000  # Convert milliseconds to seconds

    pygame.quit()  # Clean up pygame modules



if __name__=="__main__":
    main()  # Run the game if this file is executed directly

