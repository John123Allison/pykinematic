import sys
from typing import List
import pygame


def main():
    # Setup screen size
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)

    # Tutorial
    speed: List[float] = [5.0, 5.0]
    black = 0, 0, 0

    ball = pygame.image.load("assets/ball.png")
    ballrect = ball.get_rect()

    # Main loop
    while True:
        # Check for exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Move ball - look into abstracting this - the speed is an easy change
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        # Fill the screen and display
        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
