import pygame
from constants import*
from player import*
from circleshape import*
from asteroid import*
from asteroidfield import*
import sys
from Shot import*

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x=SCREEN_WIDTH /2, y=SCREEN_HEIGHT / 2)
    Shot.containers = (shots, updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000  # Limits the loop to 60 iterations per second
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("GAME OVER!")
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collide(bullet):
                    asteroid.split()
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    pygame.mixer.init(frequency=0)  # Disables sound
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    main()
    