import random
from circle import Circle
class Star(Circle):
    def __init__(self, x: float, y: float, world_width: int, world_height: int):
        super().__init__(x, y, 0, 0, 0, 2, world_width, world_height)
        self.mBrightness = random.randrange(0,255)

    def getBrightness(self) -> int:
        return self.mBrightness

    def setBrightness(self, brightness: int) -> None:
        if brightness <= 255 and brightness >= 0:
            self.mBrightness = brightness
            self.mColor = (brightness, brightness, brightness)

    def evolve(self, dt) -> None:
        choice = random.randrange(0,3)
        if choice == 1:
            self.setBrightness(self.mBrightness+10)
        elif choice == 2:
            self.setBrightness(self.mBrightness-10)
