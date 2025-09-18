from ship import Ship
from rock import Rock
from bullet import Bullet
from big_bullet import Big_bullet
from star import Star
import random
from pygame import Surface
from small_rock import Small_rock
import pygame
class Asteroids:
    def __init__ (self, world_width: int, world_height: int):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = Ship(self.mWorldWidth/2, self.mWorldHeight/2, self.mWorldWidth, self.mWorldHeight)
        self.mRocks = [Rock(random.randrange(0, self.mWorldWidth), random.randrange(0, self.mWorldHeight), self.mWorldWidth, self.mWorldHeight) for i in range(0, 10)]
        self.mBullets = []
        self.mCharge = []
        self.mStars = [Star(random.randrange(0, world_width), random.randrange(0, world_height), self.mWorldWidth, self.mWorldHeight) for i in range(0, 20)]
        self.mObjects = self.mStars + [self.mShip] + self.mBullets + self.mRocks + self.mCharge
        self.mScore = 0
        self.mShipAlive = True
        self.rock_timer = 0
    #makes it so if a rock spawns on you it will be set to inactive and not instantly spawnkill you
        for r in self.mRocks:
            if r.hits(self.mShip) == True:
                r.setActive(False)
        
    def getWorldWidth(self) -> int:
        return self.mWorldWidth
    def getWorldHeight(self) -> int:
        return self.mWorldHeight
    def getShip(self) -> Ship:
        return self.mShip
    def getRocks(self) -> list[Rock]:
        return self.mRocks
    def getBullets(self) -> list[Bullet]:
        return self.mBullets
    def getStars(self) -> list[Star]:
        return self.mStars
    def getObjects(self) -> list[object]:
        # not sure if the type hint for class should be Type or Rock, Ship :P
        return self.mObjects
    def turnShipLeft(self, delta_rotation: float):
        self.mShip.rotate(-delta_rotation)
    def turnShipRight(self, delta_rotation: float):
        self.mShip.rotate(delta_rotation)
    def accelerateShip(self, delta_velocity: float):
        self.mShip.accelerate(delta_velocity)
    def fire(self) -> None:

        if len(self.mBullets) < 3:
            z = self.mShip.fire()
            self.mBullets.append(z)
            self.mObjects.append(z)
            pygame.mixer.music.load("snd_heartshot_dr_b.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1.0)
    def charge_fire(self) -> None:

        if len(self.mBullets) < 3 and len(self.mCharge) < 1:
            z = self.mShip.charge_fire()
            self.mCharge.append(z)
            self.mObjects.append(z)
            pygame.mixer.music.load("snd_chargeshot_fire.wav")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1.0)
    def charge_sound(self) -> None:
        pygame.mixer.music.load("snd_chargeshot_charge.wav")
        pygame.mixer.music.play()
    
    def spawn_rock(self) -> None:
        choice_x = random.randint(0,2)
        choice_y = random.randint(0,2)
        
        if choice_x == 0:
            choice_x == -self.mWorldWidth
        else:
            choice_x == self.mWorldWidth
            
        if choice_y == 0:
            choice_y == -self.mWorldHeight
        else:
            choice_y == self.mWorldHeight
        r = Rock(choice_x, choice_y, self.mWorldWidth, self.mWorldHeight)
        if r.hits(self.mShip) == False:
            self.mRocks.append(r)
            self.mObjects.append(r)
            

    def evolveAllObjects(self, dt):
        for objects in self.mObjects:
            objects.evolve(dt)
        #if len(self.mRocks) < 5:
                #z = Rock(random.randrange(0, self.mWorldWidth), random.randrange(0, self.mWorldHeight), self.mWorldWidth, self.mWorldHeight)
                #self.mRocks.append(z)
                #self.mObjects.append(z)


    def collideShipAndBullets(self) -> None:
        for bullet in self.mBullets:
            if self.mShip.hits(bullet) == True and bullet.getAge() > 1:
                bullet.setActive(False)
                self.mShip.setActive(False)
                pygame.mixer.music.load("snd_explosion.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1.0)
                self.mShipAlive = False
        for charge in self.mCharge:
            if self.mShip.hits(charge) == True and charge.getAge() > 1:
                self.mShip.setActive(False)
                pygame.mixer.music.load("snd_explosion.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1.0)
                self.mShipAlive = False
    def collideShipAndRocks(self) -> None:
        for rock in self.mRocks:
            if self.mShip.hits(rock) == True:
                rock.setActive(False)
                self.mShip.setActive(False)
                pygame.mixer.music.load("snd_explosion.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1.0)
                self.mShipAlive = False

    def collideBulletsAndCharge(self) -> None:
        for bullet in self.mBullets:
            for charge in self.mCharge:
                if bullet.hits(charge) == True:
                    charge.setActive(False)
                    bullet.setActive(False)
    def collideRocksAndBullets(self) -> None:
        split_list = []
        for rock in self.mRocks:
            for bullet in self.mBullets:
                if bullet.hits(rock) == True:
                    rock.setActive(False)
                    bullet.setActive(False)
                    #this handles the score (and also what sound to play for large or small rock)
                    if isinstance(rock, Rock):
                        pygame.mixer.music.load("snd_damage_bc.wav")
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(1.0)
                        if self.mShipAlive == True:
                            self.mScore += 100
                    elif isinstance(rock, Small_rock):
                        pygame.mixer.music.load("snd_damage_bc.wav")
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.6)
                        if self.mShipAlive == True:
                            self.mScore += 50
                    if len(self.mRocks) < 18 and isinstance(rock, Small_rock) == False:

                        z = Small_rock(rock.mX-20, rock.mY, self.mWorldWidth, self.mWorldHeight)
                        split_list.append(z)
                        self.mRocks.append(z)
                        self.mObjects.append(z)
                        y = Small_rock(rock.mX+20, rock.mY, self.mWorldWidth, self.mWorldHeight)
                        split_list.append(y)
                        self.mRocks.append(y)
                        self.mObjects.append(y)





        for rock in self.mRocks:
            for charge in self.mCharge:
                if charge.hits(rock) == True:
                    rock.setActive(False)
                    pygame.mixer.music.load("snd_scytheburst.wav")
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.6)
                    if self.mShipAlive == True:
                        self.mScore += 100
                        


    def removeInactiveObjects(self) -> None:
        # have to remove inactive objects from objects list AND every other list
        for objects in self.mObjects:
            if objects.getActive() == False:
                self.mObjects.remove(objects)
        for rock in self.mRocks:
            if rock.getActive() == False:
                self.mRocks.remove(rock)
        for bullet in self.mBullets:
            if bullet.getActive() == False:
                self.mBullets.remove(bullet)
        for charge in self.mCharge:
            if charge.getActive() == False:
                self.mCharge.remove(charge)
        #not sure how to deactivate ship after death
        #if self.mShip.getActive() == False:
            #self.mShip = None



    def evolve(self, dt):
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.collideBulletsAndCharge()
        self.removeInactiveObjects()
        
        #  keeps score increasing by dt as long as ship is alive
        if self.mShipAlive == True:
            self.mScore+=dt
        
        #spawns rocks for every x amount of dt and keeps track with the rock timer

        self.rock_timer += dt
        if self.rock_timer > 5 and len(self.mRocks) < 20:
            self.spawn_rock()
            if len(self.mRocks) > 10:
                self.rock_timer = 2.5
        
    def draw(self, surface: Surface) -> None:
        rec = pygame.Rect(0, 0, self.mWorldWidth, self.mWorldHeight)
        pygame.draw.rect(surface, (0,0,0), rec)
        #draw methods below
        #gradient_colors = [(5, 7, 22), (13,16,65)] # colors used
        #num_gradient_steps = self.mWorldWidth  # Number of steps in the gradient
        #gradient_step = 1 / num_gradient_steps
        #for i in range(num_gradient_steps):
                #color = tuple(int(gradient_colors[0][c] * (1 - gradient_step * i) + gradient_colors[1][c] * gradient_step * i) for c in range(3))
                #pygame.draw.rect(surface, color, (0, i, self.mWorldWidth, 1))


        pygame.font.init() # you have to call this at the start, 
                           # if you want to use this module.
        my_font = pygame.font.SysFont('Futura', 30)

        if self.mShipAlive == False:
            self.mScore = round(self.mScore)
            text_surface = my_font.render(f"Score: {self.mScore} ", False, (255, 255, 255))

            surface.blit(text_surface, ((self.mWorldWidth/2)-50, (self.mWorldHeight/2)-50))








        #draw methods above
        for x in self.mObjects:
            if x.getActive() == True:
                x.draw(surface)
    # need to draw background everytime to prevent lines


    # evolve all objects vs evolve
    # evolve will use evolve all objects inside of it
    # evolve will call evolve all objects and then all of the collide methods.
    # collide methods will mark objects that collided as inactive
    # finish evolve with remove inactive objects




