import sys

import pygame
import pygame_gui

from object import spawn_object


def main():
    # Setup
    pygame.init()
    size = width, height = 1900, 900
    screen = pygame.display.set_mode(size)
    black = 0, 0, 0
    world_objects = []

    # TODO: Setup GUI elements
    manager = pygame_gui.UIManager(size)

    x_accel_slider_rect = pygame.Rect(30, 20, 1000, 20)
    x_acceleration_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=x_accel_slider_rect,
                                                                   start_value=0, value_range=(0, 10), manager=manager)
    x_accel_label_rect = pygame.Rect(60, 60, 40, 40)
    x_acceleration_label = pygame_gui.elements.UILabel(relative_rect=x_accel_label_rect,
                                                       text="Hello", manager=manager)

    clock = pygame.time.Clock()

    # Test spawning an obj
    world_objects = spawn_object(world_objects, 1, 0, 0, .98)

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
                        obj.accel_x = event.value * .10
                        if x_acceleration_label.text != event.value:
                            x_acceleration_label.text = event.value
            manager.process_events(event)

        # Calculate movement for each object and apply it, then render
        for obj in world_objects:
            obj.speed[0] += obj.accel_x
            obj.speed[1] += obj.accel_y

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
