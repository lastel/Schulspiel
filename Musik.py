import pygame
from LoadTextures import Tiles
import threading
import time
import random
from LoadMusic import Tracks

pygame.mixer.init()
Channel1 = pygame.mixer.Channel(1)

class Musik(threading.Thread):
    def __init__(self, playing = True):
        threading.Thread.__init__(self)
        #self.Musik = Tiles.Figur_stand
        self.running = True
        if playing == False:
            self.activated = False
        else:
            self.activated = True
            
        self.next = False

    def run(self):
        while self.running:
            if self.activated:
                if self.next:
                    Channel1.stop()
                    self.next = False
                else:
                    Channel1.unpause()
                
                if Channel1.get_busy() == 0:
                    sound = random.choice(Tracks.Tracks)
                    Channel1.play(sound)
            else:
                 Channel1.pause()
            time.sleep(0.1)


#if __name__ == "__main__":
#    thread = Musik()
#    thread.start()
    
