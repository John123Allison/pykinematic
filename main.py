import sys
from typing import List
from object import object
import pygame


def spawn_object(vel_x: float, vel_y: float, accel_x: float, accel_y: float):
    obj = object(vel_y, vel_x, accel_x, accel_y, "assets/ball.png")
    return obj


def main():
    # Setup screen size
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)

    # Objects currently in the "world"
    world_objects = []

    # Test spawning an obj
    world_objects.append(spawn_object(5.0, 5.0, 0, 0))

    # Tutorial
    black = 0, 0, 0

    # Main loop
    while True:
        # Check for exit condition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Render each object in the currently active set
        for obj in world_objects:
            obj.rect = obj.rect.move(obj.speed)
            if obj.rect.left < 0 or obj.rect.right > width:
                obj.speed[0] = -obj.speed[0]
            if obj.rect.top < 0 or obj.rect.bottom > height:
                obj.speed[1] = -obj.speed[1]

            # Fill the screen and display
            screen.fill(black)
            screen.blit(obj.surface, obj.rect)
            pygame.display.flip()


if __name__ == "__main__":
    main()
