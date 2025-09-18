import pygame
import game
import asteroids
import os
import sys
pygame.mixer.init()

class PygameApp( game.Game ):

    def __init__( self, width, height, frame_rate ):

        # title of the application is ""
        game.Game.__init__( self, "Asteroids",
                                  width,
                                  height,
                                  frame_rate )
        # create a game instance
        self.mGame = asteroids.Asteroids(width, height)
        self.charge_time = 0  
        self.max_charge_bullet = 1.5
        
        self.charge_noise_time = 0
        self.charge_noise_start = .3


        return


    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]
        
        press = pygame.key.get_pressed()
        
        if pygame.K_a in keys or pygame.K_LEFT in keys:
            self.mGame.turnShipLeft( 10.0 )
        # original value is 5.0
        
        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            self.mGame.turnShipRight( 10.0 )
        # original value is 5.0
        if pygame.K_w in keys or pygame.K_UP in keys:
            self.mGame.accelerateShip( 10.0 )
        # original value is 2.0
        if pygame.K_SPACE in newkeys:
            self.mGame.fire()

            
        if pygame.K_r in newkeys:
            os.execl(sys.executable, sys.executable, *sys.argv)
            

            
        #if pygame.K_LSHIFT in newkeys:
            #self.mGame.charge_fire()
        play_sound = False
        if press[pygame.K_SPACE]:
            self.charge_time += dt
            self.charge_noise_time += dt
            #if self.charge_noise_time >= self.charge_noise_start:
                #self.mGame.charge_sound()
                
            if self.charge_time >= self.max_charge_bullet:
                #pygame.mixer.music.stop()
                
                self.mGame.charge_fire()

        else:
            self.charge_time = 0 
            self.mcharge_noise_time = 0

        if 1 in newbuttons:
            print(self.mGame.mScore)

        self.mGame.evolve( dt )

        return

    def paint( self, surface ):
        self.mGame.draw( surface )
        return

def main():
    pygame.font.init( )
    game = PygameApp( 1400, 700, 30 )
    #1400,700,30
    game.main_loop( )

if __name__ == "__main__":
    main()
