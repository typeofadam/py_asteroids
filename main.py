# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    ### Create pygame game stuff
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    ## Create pygame groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add classes to groups
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Shot.containers = (shots, drawable, updateable)
    

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    ## Init Objects
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    ##### Game Loop ####
    while True:
        # Test if user closed game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # add background first
        
        updateable.update(dt) # update all sprites

        for asteroid in asteroids:
            if asteroid.has_collision(player):
                print("Game Over!")
                sys.exit(0)
            for shot in shots:
                if asteroid.has_collision(shot):
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)
        # ALWAYS END LOOP WITH FLIP AND TICK
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
