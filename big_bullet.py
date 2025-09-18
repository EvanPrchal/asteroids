from circle import Circle
import pygame
from pygame import Surface
class  Big_bullet(Circle):
    def __init__(self, x: float, y: float, dx: float, dy: float, rotation: float, world_width: int, world_height: int):
        super().__init__(x, y, dx, dy, rotation, 15, world_width, world_height)
        self.mAge = 0
        self.accelerate(600)
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
        if self.mAge > 6:
            self.setActive(False)
            
    def draw(self, surface: Surface) -> None:
        pygame.draw.circle(surface, (0,0,0) , [self.mX, self.mY], self.mRadius)
        pygame.draw.circle(surface, (255,255,255), [self.mX, self.mY], self.mRadius, 2)


