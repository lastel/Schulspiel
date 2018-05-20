from LoadTextures import *
import random

class Change_Texture:
    def next():
        pass

class Textures:
    run = Tiles.Figur2_run
    jump = Tiles.Figur2_jump
    stand = Tiles.Figur2_stand
    max_id = 2
    Figur_id = 2

    def update():
        for i in ["run", "jump", "stand"]:
            exec("Textures." + i + " = Tiles.Figur" + str(Textures.Figur_id) + "_" + i)

    def next():
        Textures.Figur_id += 1
        if Textures.Figur_id > Textures.max_id:
            Textures.Figur_id = 1
        Textures.update()
        

    def prev():
        Textures.Figur_id -= 1
        if Textures.Figur_id < 1:
            Textures.Figur_id = Textures.max_id
        Textures.update()

    def rand():
        Textures.Figur_id = random.randint(1, Textures.max_id)
        Textures.update()
