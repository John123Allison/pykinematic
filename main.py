import sys

import pygame

from object import spawn_object


def main():
    # Setup screen size
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    # Background color as a tuple
    black = 0, 0, 0

    # Objects currently in the "world"
    world_objects = []

    # TODO: GUI elements

    # Track time delta
    clock = pygame.time.Clock()

    # Test spawning an obj
    world_objects = spawn_object(world_objects, 5.0, 5.0, 0, 0)

    # Main loop
    while True:
        time_delta = clock.tick(60) / 1000.0

        # Handle events
        for event in pygame.event.get():
            # Check for exit condition
            if event.type == pygame.QUIT:
                sys.exit()

        # Calculate movement for each object and apply it, then renderi
        # TODO: Add in acceleration changes
        for obj in world_objects:
            # Apply movement and "bounce" off of walls
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
