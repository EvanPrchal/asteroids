from polygon import Polygon
from bullet import Bullet
from big_bullet import Big_bullet
import pygame
from pygame import Surface
class Ship(Polygon):
    def __init__(self, x: float, y: float, world_width: int, world_height: int):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        # need to set objects polygon to shape of ship for fire to work
        #self.mOriginalPolygon = [(15, 15), (-20, 30), (-5, 15), ( -19, -2.5)]
        #self.mOriginalPolygon = [(10, 10), (-10, 10), (-10, -10), ( 10, -10)]
        self.mColor = (255,255,255)
        #self.mOriginalPolygon = [(15, 0), (-30, 15), (-15, 0) ,(-30, -15)]
        self.mOriginalPolygon = [(15, 0), (-15, 15), (-30, 7.5), (-15, 0), (-30, -7.5), (-15, -15), (15,0)]
        # make sure first point is tip
        # fix and make ship cooler later
    def getX(self) -> float:
        return self.mX
    def getY(self) -> float:
        return self.mY
    def getWorldWidth(self) -> int:
        return self.mWorldWidth
    def getWorldHeight(self) -> int:
        return self.mWorldHeight
    def getPolygon(self) -> list[tuple[int, int]]:
        return self.mOriginalPolygon

    def evolve(self, dt) -> None:
        self.move(dt)
    def fire(self) -> Bullet:
        new_xy = self.rotateAndTranslatePoint(self.mOriginalPolygon[0][0], self.mOriginalPolygon[0][1])
        #self.mOriginalPolygon[0]
        return Bullet(new_xy[0], new_xy[1], self.mDX, self.mDY , self.mRotation, self.mWorldWidth, self.mWorldHeight)
    
    def charge_fire(self) -> Big_bullet:
        new_xy = self.rotateAndTranslatePoint(self.mOriginalPolygon[0][0], self.mOriginalPolygon[0][1])
        #self.mOriginalPolygon[0]
        return Big_bullet(new_xy[0], new_xy[1], self.mDX, self.mDY , self.mRotation, self.mWorldWidth, self.mWorldHeight)
    
    
    
    
    
    
    def draw(self, surface: Surface) -> None:

        point_list = self.mOriginalPolygon[:]
        z = self.rotateAndTranslatePointList(point_list)
        pygame.draw.polygon(surface, (0,0,0), z)
        pygame.draw.polygon(surface, (255,255,255), z, 2)
        

#z = Ship(5 , 5, 400, 600)
#z.fire()
#print(z.mOriginalPolygon)
