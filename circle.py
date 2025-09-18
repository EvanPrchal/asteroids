from rotatable import Rotatable
import pygame
from pygame import Color
from pygame import Surface
import random
class Circle(Rotatable):
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
        #ran = random.randrange(-100,100)
        pygame.draw.circle(surface, self.mColor, [self.mX-100, self.mY+100], self.mRadius-1)
        pygame.draw.polygon(surface, self.mColor, [(self.mX, self.mY), (self.mX-1.5, self.mY+7.5), (self.mX+1.5, self.mY+7.5)])
        pygame.draw.polygon(surface, self.mColor, [(self.mX, self.mY+15),  (self.mX-1.5, self.mY+7.5), (self.mX+1.5, self.mY+7.5)])
        pygame.draw.polygon(surface, self.mColor, [(self.mX-7.5, self.mY+7.5), (self.mX, self.mY+5), (self.mX+7.5, self.mY+7.5)])
        pygame.draw.polygon(surface, self.mColor, [(self.mX-7.5, self.mY+7.5), (self.mX, self.mY+10), (self.mX+7.5, self.mY+7.5)])
     
        
        
        
        
        
        
        #pygame.draw.polygon(surface, self.mColor, [(self.mX, self.mY), (self.mX-0.75, self.mY+3.75), (self.mX+0.75, self.mY+3.75)])
        #pygame.draw.polygon(surface, self.mColor, [(self.mX, self.mY+7.5),  (self.mX-0.75, self.mY+3.75), (self.mX+0.75, self.mY+3.75)])
        #pygame.draw.polygon(surface, self.mColor, [(self.mX-3.75, self.mY+3.75), (self.mX, self.mY+2.5), (self.mX+3.75, self.mY+3.75)])
        #pygame.draw.polygon(surface, self.mColor, [(self.mX-3.75, self.mY+3.75), (self.mX, self.mY+5), (self.mX+3.75, self.mY+3.75)])

