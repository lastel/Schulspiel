import pygame
from LoadTextures import Tiles
import threading
import time
from Figur import Figur
from LoadMusic import Sounds
import random
from Change_Texture import *

pygame.init()
pygame.mixer.init()

Channel2 = pygame.mixer.Channel(2)

class Animation(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.Animation = Textures.stand
        self.Fackelschein = Tiles.Fackelschein
        self.sound = True

    def run(self):
        while 1:
            if Figur.jumping or not Figur.can_jump:
                if (Figur.jump_timer >= 0 and Figur.jump_timer <=
                    Figur.max_jump_timer / 2 * 0.3):
                    self.Animation = Textures.jump[0]
                elif (Figur.jump_timer >= Figur.max_jump_timer / 2 * 0.4
                      and Figur.jump_timer <=
                      Figur.max_jump_timer / 2 * 0.7):
                    self.Animation = Textures.jump[1]
                else:
                    self.Animation = Textures.jump[2]
                    
            elif Figur.running:
                for i in Textures.run:
                    if not Figur.jumping:
                        self.Animation = i
                        if self.sound == True:
                            random_sound = random.choice(Sounds.Walk_Stone)
                            Channel2.play(random_sound)
                        time.sleep(0.1)

            else:
                self.Animation = Textures.stand

            
            r = random.choice(Tiles.Fackelscheine)
            self.Fackelschein = r
            
            time.sleep(0.1)
    
