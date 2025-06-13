import pygame
import sys
from databases import *
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #create a clock to manage framerate
    clock=pygame.time.Clock()
    #set a delta time variable
    dt=0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()   
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        
        screen.fill((0,0,0))
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit framerate to 60 fps
        dt=clock.tick(60)/1000

    
    pygame.quit()



if __name__=="__main__":
    main()

