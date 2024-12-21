import pygame
from player import Player
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # 1280 x 720 px
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        # Basic black screen fill
        pygame.Surface.fill(screen, (0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        dt += clock.tick(60) / 1000

if __name__ == "__main__":
    main()
