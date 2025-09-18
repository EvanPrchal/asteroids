from rotatable import Rotatable
import pygame
from pygame import Color
from pygame import Surface
class Bullet_shape(Rotatable):
    def __init__(self, x: float, y: float, dx: float, dy: float, rotation: float, radius: float, world_width: int, world_height: int):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mRadius = radius
        self.mColor = (255, 255, 255)

    def getRadius(self) -> float:
        return self.mRadius

    def getColor(self) -> Color:
        return self.mColor

    def setRadius(self, radius: float) -> None:
        if radius >= 1:
            self.mRadius = radius

    def setColor(self, color: Color) -> None:
        self.mColor = color

    def draw(self, surface: Surface) -> None:
        pygame.draw.ellipse(surface, self.mColor, (100, 100, 200, 100))

