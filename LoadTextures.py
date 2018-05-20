import pygame
import os

pygame.init()

path = str(os.path.abspath(".") + "/Textures/")

class Tiles:

    path = path
    Size = 64

    def Load_Texture(file, Size, Size2 = 0):
        if Size2 == 0:
            Size2 = Size
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size2))
        #surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface = pygame.Surface((Size, Size2), pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface

    Stein = Load_Texture(path + "Stone.png", Size)
    Gras = Load_Texture(path + "Boden_Gras.png", Size)
    Figur = Load_Texture(path + "Figur.png", Size, Size * 2)
    Sonne = Load_Texture(path + "Sonne.png", Size * 2)
    Sound_Muted = Load_Texture(path + "Sound_Muted.png", Size)
    Music_Paused = Load_Texture(path + "Music_Paused.png", Size)
    Fackelschein = Load_Texture(path + "Fackelschein_alt.png", Size * 10)
    Fackelschein2 = pygame.transform.flip(Fackelschein, True, False)
    Fackelschein3 = pygame.Surface(
        (Fackelschein.get_width(), Fackelschein.get_height()), pygame.SRCALPHA)
    Fackelschein3.blit(Fackelschein, (0, 0))
    Fackelschein3.blit(Fackelschein2, (0, 0))
    Fackelscheine = [Fackelschein]#, Fackelschein2, Fackelschein3]
    Fackelscheine2 = [Fackelschein, Fackelschein2]#, Fackelschein3]
    
    Abdeckung = Load_Texture(path + "Abdeckung.png", Size * 30)

    Figur1_run1 = Load_Texture(path + "Player_1/Player_run1.png", Size, Size * 2)
    Figur1_run2 = Load_Texture(path + "Player_1/Player_run2.png", Size, Size * 2)
    Figur1_run3 = Load_Texture(path + "Player_1/Player_run3.png", Size, Size * 2)
    Figur1_run4 = Load_Texture(path + "Player_1/Player_run4.png", Size, Size * 2)
    Figur1_run5 = Load_Texture(path + "Player_1/Player_run5.png", Size, Size * 2)
    Figur1_run6 = Load_Texture(path + "Player_1/Player_run6.png", Size, Size * 2)

    Figur1_jump1 = Load_Texture(path + "Player_1/Player1_jump1.png", Size, Size * 2)
    Figur1_jump2 = Load_Texture(path + "Player_1/Player1_jump2.png", Size, Size * 2)
    Figur1_jump3 = Load_Texture(path + "Player_1/Player1_jump3.png", Size, Size * 2)
    Figur1_stand = Load_Texture(path + "Player_1/Player_Stand.png", Size, Size * 2)

    
    Figur2_run1 = Load_Texture(path + "Player_Miner/Player_Miner_run1.png", Size, Size * 2)
    Figur2_run2 = Load_Texture(path + "Player_Miner/Player_Miner_run2.png", Size, Size * 2)
    Figur2_run3 = Load_Texture(path + "Player_Miner/Player_Miner_run3.png", Size, Size * 2)
    Figur2_run4 = Load_Texture(path + "Player_Miner/Player_Miner_run4.png", Size, Size * 2)
    Figur2_run5 = Load_Texture(path + "Player_Miner/Player_Miner_run5.png", Size, Size * 2)
    Figur2_run6 = Load_Texture(path + "Player_Miner/Player_Miner_run6.png", Size, Size * 2)
    
    Figur2_jump1 = Load_Texture(path + "Player_Miner/Player_Miner_jump1.png", Size, Size * 2)
    Figur2_jump2 = Load_Texture(path + "Player_Miner/Player_Miner_jump2.png", Size, Size * 2)
    Figur2_jump3 = Load_Texture(path + "Player_Miner/Player_Miner_jump3.png", Size, Size * 2)
    Figur2_stand = Load_Texture(path + "Player_Miner/Player_Miner_stand.png", Size, Size * 2)
    

    Figur1_run = [Figur1_run1, Figur1_run2, Figur1_run3, Figur1_run4, Figur1_run5,
                 Figur1_run6]
    Figur1_jump = [Figur1_jump1, Figur1_jump2, Figur1_jump3]

    Figur2_run = [Figur2_run1, Figur2_run2, Figur2_run3, Figur2_run4, Figur2_run5,
                 Figur2_run6]
    Figur2_jump = [Figur2_jump1, Figur2_jump2, Figur2_jump3]



    Texture_Tags = {"1" : Stein, "2" : Gras}
