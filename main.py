import pygame

from asteroid import *
from asteroidfield import *
from circleshape import *
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()

    Player.containers = (group_drawable, group_updatable)
    Asteroid.containers = (
        group_asteroids, 
        group_drawable, 
        group_updatable
    )
    AsteroidField.containers = (group_updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        group_updatable.update(dt)
        #Set background color, draw on this
        screen.fill("black")

        for drawable in group_drawable:
            drawable.draw(screen)
        pygame.display.flip()

        #End of the game loop
        dt = clock.tick(60) / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()