import math
from movable import Movable
class Rotatable(Movable):
    def __init__(self, x: float, y: float, dx: float, dy: float, rotation: float, world_width: int, world_height: int):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation
    
    def getX(self) -> float:
        return self.mX
    def getY(self) -> float:
        return self.mY
    def getDX(self) -> float:
        return self.mDX
    def getDY(self) -> float:
        return self.mDY
    def getWorldWidth(self) -> int:
        return self.mWorldWidth
    def getWorldHeight(self) -> int:
        return self.mWorldHeight
    def getRotation(self) -> float:
        return self.mRotation
    
    def rotate(self, delta_rotation: float) -> None:
        pass
        #if self.mRotation + delta_rotation >= 360:
            #self.mRotation = self.mRotation + delta_rotation - 360
        #elif self.mRotation + delta_rotation < 0:
            #self.mRotation = self.mRotation + delta_rotation + 360
        #else:
            #self.mRotation += delta_rotation
        self.mRotation = (self.mRotation + delta_rotation) % 360.0    
            
            
    def splitDeltaVIntoXAndY(self, rotation: float, delta_velocity: float) -> tuple[float, float]:
        radians = math.radians(rotation)
        cosine = math.cos(radians)
        sine = math.sin(radians)
        x = cosine * delta_velocity
        y = sine * delta_velocity
        return (x, y)
        
    
    def accelerate(self, delta_velocity: float) -> None:
        hoz_vert = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        x = hoz_vert[0]
        y = hoz_vert[1]
        self.mDX += x
        self.mDY += y
        
        
    def rotatePoint(self, x: float, y: float) -> tuple[float, float]:
        #
        #
        #
        #
        #
        radians = math.radians(self.mRotation)
        #cosine = math.cos(radians)
        #sine = math.sin(radians)
        new_x = math.cos(radians) * x - math.sin(radians) * y
        new_y = math.sin(radians) * x + math.cos(radians) * y
        #new_x = cosine * x + sine * y
        #new_y = sine * x - cosine * y

        return(new_x, new_y)
    
    def translatePoint(self, x: float, y: float) -> tuple[float, float]:
        x += self.mX
        y += self.mY
        return(x, y)
    
    def rotateAndTranslatePoint(self, x: float, y: float) -> tuple[float, float]:
        z = self.rotatePoint(x, y)
        return self.translatePoint(z[0], z[1])
    
    def rotateAndTranslatePointList(self, point_list: list[tuple[float, float]]) -> list[tuple[float, float]]:
        counter = 0
        lister = []
        for x in point_list:
            z = self.rotateAndTranslatePoint(point_list[counter][0], point_list[counter][1])
            lister.append(z)
            counter += 1
        return lister
    



#test = Rotatable(50, 50, 1.5, 2.5, 90, 400, 600)
#a = [(10,15),(2,25)]
#print(test.rotateAndTranslatePointList(a))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

    
    
    
