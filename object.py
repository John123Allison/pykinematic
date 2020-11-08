from typing import List

from pygame import Rect, Surface
import pygame


class object:
    """
    A physical object in the world. Has attributes for velocity in X and Y, acceleration in X and Y,
    and a related asset. The object does not actually get drawn on the screen, but is instead a
    centralized store of information for objects that will be handled by PyGame.
    """
    speed: List[float]
    accel_x: float
    accel_y: float
    surface: Surface
    rect: Rect

    def __init__(self, velocity_x: float, velocity_y: float, accel_x: float, accel_y: float, asset_path: str):
        self.speed = [velocity_x, velocity_y]
        self.accel_x = accel_x
        self.accel_y = accel_y
        self.surface = pygame.image.load(asset_path)
        self.rect = self.surface.get_rect()
