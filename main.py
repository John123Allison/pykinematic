import sys

import pygame
import pygame_gui

from object import spawn_object


def main():
    # Setup screen size
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    # Background color as a tuple
    black = 0, 0, 0

    # Objects currently in the "world"
    world_objects = []

    # GUI manager
    manager = pygame_gui.UIManager((800, 600))
    clock = pygame.time.Clock()

    # FIXME: Problem with library? Who can know.
    # Add a button the screen
    hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                                text='Say Hello',
                                                manager=manager)

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
            # Handle button presses
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        print('Hello World!')
            # Handle GUI updates
            manager.process_events(event)

        # Calculate movement for each object and apply it, then render
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

        # Update and draw GUI
        manager.update(time_delta)
        manager.draw_ui(screen)


if __name__ == "__main__":
    main()
