import pygame
import os

pygame.mixer.init()

path = str(os.path.abspath(".") + "/Sounds/")

class Tracks:
    
    Music1 = pygame.mixer.Sound(path + "Music1.ogg")
    Music2 = pygame.mixer.Sound(path + "Music2.ogg")

    Tracks = [Music1, Music2]

class Sounds:
    
    walk1 = pygame.mixer.Sound(path + "Walking1.ogg")
    walk2 = pygame.mixer.Sound(path + "Walking2.ogg")
    
    Walk_Stone = [walk1, walk2]
    
