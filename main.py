import sys

import pygame
import pygame_gui

from object import spawn_object

GRAVITY = 9.8
SCALE_FACTOR = .1

"""
TODO: Look into ways to abstract some of the code into different functions,
      read docs to figure out how to manage state more effectively.
"""
def main():
    # Setup
    pygame.init()
    size = width, height = 1500, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyKinematic")
    black = 0, 0, 0
    world_objects = []

    # Setup GUI elements
    # TODO: Add labels for sliders
    manager = pygame_gui.UIManager(size)

    x_accel_slider_rect = pygame.Rect(30, 20, 1000, 20)
    x_acceleration_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=x_accel_slider_rect,
                                                                   start_value=0, value_range=(0, 10), manager=manager)
    y_accel_slider_rect = pygame.Rect(30, 40, 1000, 20)
    y_acceleration_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=y_accel_slider_rect,
                                                                   start_value=0, value_range=(0, 10), manager=manager)

    clock = pygame.time.Clock()

    # Test spawning an obj
    world_objects = spawn_object(world_objects, 1, 0, 0, 0)

    # Main loop
    while True:
        time_delta = clock.tick(60) / 1000.0

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Handle x_acceleration_slider changes
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == x_acceleration_slider:
                        obj.accel[0] = event.value * SCALE_FACTOR
                    if event.ui_element == y_acceleration_slider:
                        obj.accel[1] = event.value * SCALE_FACTOR

            manager.process_events(event)

        # Calculate movement for each object and apply it, then render
        for obj in world_objects:
            # TODO: Add in air resistance
            obj.speed[0] += obj.accel[0]
            obj.speed[1] += obj.accel[1]
            
            # TODO: adjust collision to not cause The Issue
            obj.rect = obj.rect.move(obj.speed)
            if obj.rect.left < 0 or obj.rect.right > width:

                obj.speed[0] = -obj.speed[0]
            if obj.rect.top < 0 or obj.rect.bottom > height:
                obj.speed[1] = -obj.speed[1] 

            screen.fill(black)
            screen.blit(obj.surface, obj.rect)

        # Update the screen
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
