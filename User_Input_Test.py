from Keybinding import *
import pygame
from pygame.locals import *

running = True
a = pygame.display.set_mode()
data_to_dict(load_data(path))
Key.Keys_now = copy.deepcopy(Key.Keys)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            key = event.key
            if key in Key.Keys["forward"]:
                print("%s (Forward)" % int_to_key(event.key))
                
            elif key in Key.Keys["backward"]:
                print("%s (Backward)" % int_to_key(event.key))
                
            elif key in Key.Keys["jump"]:
                print("%s (Jump)" % int_to_key(event.key))
                
            else:
                print(int_to_key(event.key))

pygame.quit()
