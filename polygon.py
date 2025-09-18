import pygame
from pygame import Surface
from rotatable import Rotatable
import math
class Polygon(Rotatable):
    def __init__(self, x: float, y: float, dx: float, dy: float, rotation: float, world_width: int, world_height: int):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)

        self.mOriginalPolygon: list[tuple[int, int]] = []
        self.mColor = (255, 255, 255)

    def getPolygon(self) -> list[tuple[int, int]]:
        return self.mOriginalPolygon
    def getColor(self) -> tuple[int,int,int]:
        return self.mColor


    def setPolygon(self, point_list: list[tuple[int, int]]) -> None:
        self.mOriginalPolygon = point_list
    def setColor(self, color):
        self.mColor = color

    def draw(self, surface: Surface) -> None:
        # fix later lmaoooo
       # self.mOriginalPolygon = self.rotateAndTranslatePointList(self.mX, self.mY)
       # pygame.draw.polygon(surface, self.mColor, (self.mOriginalPolygon))


        #average_count = 0
        #rad_counts = 0
        #avg = 0
        #index_counter = 0
        #point_list = []
        #for x in self.mOriginalPolygon:
        #index_counter += #1
        point_list = self.mOriginalPolygon[:]
        z = self.rotateAndTranslatePointList(point_list)
       # for point in self.mOriginalPolygon:

           # new_xy = self.rotateAndTranslatePointList((point[0], point[1]))
           # point_list.extend(new_xy)
        pygame.draw.polygon(surface, self.mColor, z)



        #trans_xy = self.rotateAndTranslatePointList(self.mOriginalPolygon[0])
       # pygame.draw.polygon(surface, self.mColor, trans_xyy)
        #print(points)
        #pygame.draw.polygon(surface, self.mColor, points)

    def getRadius(self) -> float:
        # find average of radiuses
        # polygon points are all based around the origin, center is always origin no matter what
        # use pythagorean theorem, a**2 + b**2 = c**
        # c = sqrt(a**2 + b**2), c = radius
        average_count = 0
        rad_counts = 0
        avg = 0
        index_counter = 0
        for point in self.mOriginalPolygon:
            radius = math.sqrt(self.mOriginalPolygon[index_counter][0]**2 + self.mOriginalPolygon[index_counter][1]**2)
            rad_counts += radius
            average_count += 1
            index_counter += 1
            avg = rad_counts / average_count
        return avg

        #loop over all points and average















