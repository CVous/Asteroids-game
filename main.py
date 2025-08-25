import pygame
from constants import *
from player import player
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()


    my_player = player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0

    while True:  
        dt = clock.tick(60) / 1000  #set to 60 fps limit 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        
        
        
        # v put last -- updates to next frame
        pygame.display.flip()
        

        



if __name__ == "__main__":
    main()
