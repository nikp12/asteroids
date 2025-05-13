import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from shot import *

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        for asteroid in asteroids:
            collide = asteroid.detect_collision(player)
            if collide == True:
                print("Game over!")
                quit()
            for shot in shots:
                asteroid_shot = asteroid.detect_collision(shot)
                if asteroid_shot == True:
                    asteroid.split()
        dt = clock.tick(60) / 1000.0
        

if __name__ == "__main__":
    main()