from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    conti = True
    x=int(SCREEN_WIDTH/2)
    y=int(SCREEN_HEIGHT/2)
    print(type(x))
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    dt = 0.0
    # Insert objects into a group so DRY is maintained
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots =pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField.containers = (updatable)
    print(drawable.sprites())    
    space_ship = Player(x,y)
    sp_asteroid = AsteroidField()
    while conti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            conti = space_ship.collide(obj)
            if not conti:
              print("GAME OVER")
              exit()
            for shot in shots:
                if not shot.collide(obj):
                    obj.split()
                    shot.kill()
            
        pygame.display.flip()
        dt = (game_time.tick(60))/1000
if __name__ == "__main__":
   main()
