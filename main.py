import sys

import pygame
import pygame_gui

from object import spawn_object


def main():
    pygame.init()

    # Setup screen size
    size = width, height = 1900, 1000
    screen = pygame.display.set_mode(size)
    # Background color as a tuple
    black = 0, 0, 0

    # Objects currently in the "world"
    world_objects = []

    # TODO: GUI elements
    manager = pygame_gui.UIManager(size)
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1800, 50), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)

    # Track time delta
    clock = pygame.time.Clock()

    # Test spawning an obj
    world_objects = spawn_object(world_objects, 0, 0, 0, .98)

    # Main loop
    while True:
        time_delta = clock.tick(60) / 1000.0

        # Handle events
        for event in pygame.event.get():
            # Check for exit condition
            if event.type == pygame.QUIT:
                sys.exit()
            # Handle GUI events
            manager.process_events(event)

        # Calculate movement for each object and apply it, then renderi
        for obj in world_objects:
            # Apply acceleration to object's movement
            obj.speed[0] += obj.accel_x
            obj.speed[1] += obj.accel_y
            # Apply movement and "bounce" off of walls
            obj.rect = obj.rect.move(obj.speed)
            if obj.rect.left < 0 or obj.rect.right > width:
                obj.speed[0] = -obj.speed[0]
            if obj.rect.top < 0 or obj.rect.bottom > height:
                obj.speed[1] = -obj.speed[1]
            # Fill the screen and display
            screen.fill(black)
            screen.blit(obj.surface, obj.rect)

        # Handle GUI updates
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
