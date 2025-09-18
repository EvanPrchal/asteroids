from pygame import Surface

import math
class Movable:
    def __init__(self, x: float, y: float, dx: float, dy: float, world_width: int, world_height: int):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive = True
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
    def getActive(self) -> bool:
        return self.mActive
    def setActive(self, active: bool) -> None:
        self.mActive = active
    def move(self, dt: float) -> None:
        self.mX = self.mX + dt * self.mDX
        self.mY = self.mY + dt * self.mDY
        #mx must be >= 0 and less than worldwidth
        #my must be >= 0 and less than worldheight

        #might need to change this to be ahead of the self.mZ = self.mZ + dt * self.mDZ formula for it to work?
        #like if self.mZ + dt * self.mDZ < 0, or if > width/height change it then, else change normally
        #check rotatable.py for structure if needed
        if self.mX < 0:
            self.mX = self.mX + self.mWorldWidth
        if self.mX >= self.mWorldWidth:
            self.mX = self.mX - self.mWorldWidth
        # can mod by width and height i think instead similar to rotate?
        # said smth about mod by maximums
        if self.mY < 0:
            self.mY = self.mY + self.mWorldHeight
        if self.mY >= self.mWorldHeight:
            self.mY = self.mY - self.mWorldHeight

    def hits(self, other: "Movable") -> bool:
        # use class name in quotes for type hint if using type hint in its own class
        distance = math.sqrt((other.getX()-self.mX)**2 + (other.getY() - self.mY)**2)
        if distance <= other.getRadius() + self.getRadius():
            return True
        else:
            return False
    # want to know if 2 objects collide
    # good for circles, objects all have an x and y position
    # imagine x and y is in center
    # distance from center of circle to center of othre circle, as well as each circles radius
    #find distance, take the radius, add em together, and its less than distance theyve collided
    # d = sqrt(x2-x1)2 + ()2
    # if distance <= r1 + r2, theyve collided


    def accelerate(self, delta_velocity: int) -> None:
        raise NotImplementedError()

    def evolve(self, dt: float) -> None:
        raise NotImplementedError()

    def draw(self, surface: Surface) -> None:
        raise NotImplementedError()

    def getRadius(self) -> None:
        raise NotImplementedError()






