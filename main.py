import pygame
import sys
from constants import *
from player import player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)



    my_player = player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0

    while True:  
        dt = clock.tick(60) / 1000  #set to 60 fps limit 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if my_player.collision_check(asteroid):  
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_check(asteroid):
                    asteroid.split()
                    shot.kill()
                    
            

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        
        
        
        # V put last -- updates to next frame
        pygame.display.flip()
        

        



if __name__ == "__main__":
    main()
