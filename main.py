from constants import *
import pygame
from player import Player
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    conti = True
    x=int(SCREEN_WIDTH/2)
    y=int(SCREEN_HEIGHT/2)
    print(type(x))
    space_ship = Player(x,y)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    dt = 0
    while conti:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        space_ship.draw(screen)
        pygame.display.flip()
        dt = game_time.tick(60)/1000
if __name__ == "__main__":
    main()
