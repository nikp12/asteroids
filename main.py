import pygame
from constants import *
from player import *
from circleshape import *

updatable = pygame.sprite.Group()
updatable.add(Player)
drawable = pygame.sprite.Group()
drawable.add(Player)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, color="black")
        updatables.update(dt)
        drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0
        

if __name__ == "__main__":
    main()