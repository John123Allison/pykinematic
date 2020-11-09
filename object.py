from typing import List

import pygame


class PhysicsObject:
    """
    A physical object in the world. Has attributes for velocity in X and Y, acceleration in X and Y,
    and a related asset. The object does not actually get drawn on the screen, but is instead a
    centralized store of information for objects that will be handled by PyGame.

    :param velocity_x The object's x velocity
    :param velocity_y The object's y velocity
    :param accel_x The object's x acceleration
    :param accel_y The object's y acceleration
    :param asset_path Local path to the object's associated visual asset
    """
    speed: List[float]
    accel_x: float
    accel_y: float
    surface: pygame.Surface
    rect: pygame.Rect

    def __init__(self, velocity_x: float, velocity_y: float, accel_x: float, accel_y: float, asset_path: str):
        self.speed = [velocity_x, velocity_y]
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.surface = pygame.image.load(asset_path)
        self.rect = self.surface.get_rect()


def spawn_object(objects, vel_x: float, vel_y: float, accel_x: float, accel_y: float) -> List[PhysicsObject]:
    """
    Takes a list of physics objects as a parameter and then returns a list appended with a new 
    object with the given parameters. 
    """
    obj = PhysicsObject(vel_y, vel_x, accel_x, accel_y, "assets/ball.png")
    objects.append(obj)
    return objects
