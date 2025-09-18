import math
from polygon import Polygon
import random
import pygame
from pygame import Surface
class Rock(Polygon):
    def __init__(self, x: float, y: float, world_width: int, world_height: int):
        super().__init__(x, y, 0, 0, random.uniform(0, 359.9), world_width, world_height)
        self.mSpinRate = random.uniform(-90, 90)
        #self.accelerate(random.uniform(10,20))
        self.accelerate(random.uniform(30,100))

        self.setPolygon(self.createRandomPolygon(30, 10))
        self.mColor = (0,0,0)
    def getSpinRate(self) -> float:
        return self.mSpinRate
    def setSpinRate(self, spin_rate: float) -> None:
        self.mSpinRate = spin_rate

    def createRandomPolygon(self, radius: int, number_of_points: int) -> list[tuple[int]]:
        # used for setting the objects polygon to the shape of a random rock
        # pygame.draw.polygon(surface, self.Color, (self.mOriginalPolygon))
        # degrees / num_of_points
        # .7 or 1.3 of radius for each points for radius
        # to find angle its 360 / num of points
        # convert angle into radians (probably)
        # for each point in num of points,  rand uniform .7 - 1.3 * radius
        # for i in range (numPOints)
        # x = cosine(angle * i) * radius
        # y = sin(angle * i) * radius
        # add x and y to our points
        point_list = []
        for i in range(0, number_of_points):
            rads = random.uniform(.7, 1.3) * radius
            angle = 360/number_of_points
            angle = math.radians(angle)
            x = math.cos(angle*i) * rads
            y = math.sin(angle*i) * rads
            tup = (x, y)
            point_list.append(tup)

        return point_list
    def evolve(self, dt: float) -> None:
        self.move(dt)
        self.rotate(dt*self.mSpinRate)
        
        
        
        
     
    def draw(self, surface: Surface) -> None:

        point_list = self.mOriginalPolygon[:]
        z = self.rotateAndTranslatePointList(point_list)
        pygame.draw.polygon(surface, self.mColor, z)
        pygame.draw.polygon(surface, (255,255,255), z, 1)

