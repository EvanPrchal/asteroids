from circle import Circle
from bullet_shape import Bullet_shape
from pygame import Surface
import pygame
class  Bullet(Circle):
    def __init__(self, x: float, y: float, dx: float, dy: float, rotation: float, world_width: int, world_height: int):
        super().__init__(x, y, dx, dy, rotation, 4, world_width, world_height)
        self.mAge = 0
        self.accelerate(500)
        self.move(.1)
        #change to 2552550 later for yellow
        self.mColor = (255,255,255)
        
    def getAge(self) -> float:
        return self.mAge

    def setAge(self, age: int) -> None:
        self.mAge = age

    def evolve(self, dt) -> None:
        self.move(dt)
        self.mAge+=dt
        if self.mAge > 2:
            self.setActive(False)
            
    def draw(self, surface: Surface) -> None:
        """if self.mRotation >= 0 and self.mRotation <= 180:
            pygame.draw.ellipse(surface, self.mColor, [self.mX, self.mY, 20, 10])
        elif self.mRotation >= 181 and self.mRotation <= 360:
            pygame.draw.ellipse(surface, self.mColor, [self.mX, self.mY, 10, 20])"""

            

        pygame.draw.circle(surface, self.mColor, [self.mX, self.mY], self.mRadius)


