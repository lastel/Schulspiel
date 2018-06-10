import pygame
import random, sys, time
import modules
from pygame.locals import *
from LoadTextures import Tiles
from Figur import Figur
from Animation import Animation
from Musik import Musik
from Write_score import *
from Keybinding import *
from Change_Texture import *
from Exec_Shell import *
#import LoadTextures

pygame.init()
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

clock = pygame.time.Clock()
Font = pygame.font.SysFont("arial", 20)
Font_50 = pygame.font.SysFont("arial", 50)
Font_80 = pygame.font.SysFont("arial", 80)
Font_100 = pygame.font.SysFont("arial", 100)
Font_130 = pygame.font.SysFont("arial", 130)
Font_200 = pygame.font.SysFont("arial", 200)

Size = Tiles.Size

SpielFeld = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#, pygame.RESIZABLE)
SpielFeld = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Jump and run")

display_width = pygame.display.get_surface().get_width()
display_height = pygame.display.get_surface().get_height()

WEISS = (255, 255, 255)
BLAU = 	(0,0,102)
RED = (255, 0, 0)
SCHWARZ = (0, 0, 0)
GRAU = (190, 190, 190)
GREEN = (0,128,0)

Animation_thread = Animation()
Animation_thread.start()

Musik_thread = Musik(False)
Musik_thread.start()

ExecShell = ExecuteShell()
ExecShell.daemon = True
ExecShell.start()

SpielFeld.fill(WEISS)

pygame.display.update()

mainloop2 = True
lost = False
normal = False
Tutorial_die = False

HitBox_showing = False
Borders_active = False
Circle_Hitbox = False

path_kb = str(os.path.abspath(".") + r"\Keybindings.txt")
data_to_dict(load_data(path_kb))
Key.Keys_now = copy.deepcopy(Key.Keys)

while mainloop2:
    music_activated = Musik_thread.activated
    if not Tutorial_die:
        Musik_thread.activated = False
    mainscreen = False

    if normal:
        SpielFeld.fill(SCHWARZ)
        normal_x = 0
        pygame.display.update()
        time.sleep(1)
        if HitBox_showing:
            Borders_active = True
    else:
        normal_x = 0
        
    if not normal and not Tutorial_die:
        mainscreen = True
        game_mode = False

        Titlescreen = Tiles.Load_Texture(
            Tiles.path + "Titlescreen.png", display_height, display_height)
        SpielFeld.fill(SCHWARZ)
        SpielFeld.blit(Titlescreen, (
            (display_width - display_height) / 2, -30))#SpielFeld.fill(GREEN)
        s = pygame.Surface((350, 60))
        s.fill(GRAU)
        y_height = 410
        x = display_width / 2 - s.get_width() / 2
        y = y_height - s.get_height() / 2
        x_end = x + s.get_width()
        y_end = y + s.get_height()
        
        SpielFeld.blit(s, (x, y))
        message_overlay = Font_50.render("Play", True, SCHWARZ)
        
        x2 = display_width / 2 - message_overlay.get_width() / 2
        y2 = y_height - message_overlay.get_height() / 2
        SpielFeld.blit(message_overlay, (x2, y2))

        s2 = pygame.Surface((350, 60))
        s2.fill(GRAU)
        y_height = y_end + 40
        x3 = display_width / 2 - s2.get_width() / 2
        y3 = y_height - s2.get_height() / 2
        x3_end = x3 + s2.get_width()
        y3_end = y3 + s2.get_height()
        
        SpielFeld.blit(s2, (x3, y3))
        message_overlay = Font_50.render("Story", True, SCHWARZ)
        
        x2 = display_width / 2 - message_overlay.get_width() / 2
        y2 = y_height - message_overlay.get_height() / 2
        SpielFeld.blit(message_overlay, (x2, y2))
        
        if lost:
            lost_message_overlay = Font_100.render("You Lost!", True, (RED))
            Score_overlay = Font_80.render(message, True, (GREEN))
            SpielFeld.blit(
                lost_message_overlay, (
                    (display_width - lost_message_overlay.get_width()) / 2, 40))
            SpielFeld.blit(
                Score_overlay, (
                    (display_width - Score_overlay.get_width()) / 2, 
                                       (display_height -
                                        Score_overlay.get_height()) / 2 + 50))

            if rank == 1:
                message_overlay = Font_100.render("NEW HIGHSCORE!", True, (GREEN))
                SpielFeld.blit(
                message_overlay, (
                    (display_width - message_overlay.get_width()) / 2, 
                                       (display_height -
                                        message_overlay.get_height()) / 2 + 140))
            else:
                highscore = Scores.highscore()
                message = ("The Highscore is %s!" % int(highscore))
                message_overlay = Font_80.render(message, True, (GREEN))
                SpielFeld.blit(
                message_overlay, (
                    (display_width - message_overlay.get_width()) / 2, 
                                       (display_height -
                                        message_overlay.get_height()) / 2 + 140))

        pygame.display.update()

        mainloop = True
        
        while mainscreen:
            for event in pygame.event.get():
                if event.type == QUIT:
                    mainscreen = False
                    mainloop2 = False
                    
                elif event.type == MOUSEBUTTONDOWN:
                    if (event.pos[0] >= x and
                        event.pos[0] <= x_end and
                        event.pos[1] >= y and
                        event.pos[1] <= y_end
                        ):
                        game_mode = 1
                        mainscreen = False
                        
                    elif (event.pos[0] >= x3 and
                          event.pos[0] <= x3_end and
                          event.pos[1] >= y3 and
                          event.pos[1] <= y3_end
                        ):
                        game_mode = 2
                        mainscreen = False
                        Levels = [modules.Modules.Tutorial]
                        Levels2 = Levels
                        Bilder = ["Comic1.png", "Comic2.png", "Comic3.png"]
                        SpielFeld.fill(SCHWARZ)
                        pygame.display.update()
                        time.sleep(2)
                        for i in Bilder:
                            if mainloop:
                                SpielFeld.fill(SCHWARZ)
                                pygame.display.update()
                                time.sleep(0.8)
                                Picture = Tiles.Load_Texture(
                                Tiles.path + i, display_height,
                                display_height)
                                SpielFeld.fill(SCHWARZ)
                                SpielFeld.blit(Picture, (
                                (display_width - display_height) / 2, -30))
                                messages = []
                                if i == Bilder[0]:
                                    messages = [
                                    "Peter ist gerade untertage und baut Erze ab,",
                                    "sein Freund kommt um ihm zu helfen, als er",
                                    "fast da ist, stolpert sein Freund über einen",
                                    "Stein, der am Boden liegt.",
                                    "Er fällt gegen einen Pfosten, der durchbricht."
                                    ]
                                    
                                if i == Bilder[1]:
                                    messages = [
                                    "Ausgerechnet hat dieser Pfosten",
                                    "einen Teil der Decke gehalten.",
                                    "Die Decke stürtzt hinab und erschlägt",
                                    "Peters Freund."
                                    ]
                                    
                                if i == Bilder[2]:
                                    messages = [
                                    "Peter kann seinem Freund nicht mehr helfen",
                                    "und der Steinschlag versperrt ihm leider",
                                    "auch noch den Weg zurück.",
                                    "Also muss Peter noch tiefer in die",
                                    "Höhle hinein."
                                    ]

                                counter = 0
                                for message in messages:
                                    message_overlay = Font_50.render(message, True, (RED))
                                    SpielFeld.blit(message_overlay, (
                                        display_width / 2 - (message_overlay.get_width()) / 2, 
                                        display_height - int(len(messages) / 5 * 400) + counter * 80 - (
                                        message_overlay.get_height()) / 2))
                                    counter += 1
                                    
                                pygame.display.update()
                                clicked = False
                                while not clicked:
                                    for event in pygame.event.get():
                                        if event.type == MOUSEBUTTONDOWN:
                                            clicked = True
                                            #print(event.pos[0], event.pos[1])
                                        if event.type == QUIT:
                                            mainscreen = False
                                            mainloop2 = False
                                            mainloop = False
                                            clicked = True
                                            break
                                        if event.type == KEYDOWN:
                                            if event.key == pygame.K_ESCAPE:
                                                mainloop = False
                                                clicked = True
                                                break

                                if mainloop:
                                    pass#time.sleep(3)
                                else:
                                    break
                                        
                                        
                        if mainloop:   
                            SpielFeld.fill(SCHWARZ)
                            pygame.display.update()
                            time.sleep(0.8)
                        


        if not mainloop2:
            break
    else:
        if Tutorial_die:
            game_mode = 2
        else:
            game_mode = 1        
        normal = False
        Tutorial_die = False
        mainloop = True
    Musik_thread.activated = music_activated
        
    if game_mode == False:
        game_mode = 2

    if game_mode == 1:
        Figur.y = Size * 5 - Size / 8#display_height - (Size * 10)
        Figur.x = 0
    else:
        Figur.y = Size * 6 - Size / 8#display_height - (Size * 10)
        Figur.x = 0
        
    
    Figur.Links = False
    Figur.Rechts = False
    
    lost = False
    Score = 0

    cSec = 0
    FPScount = 0
    deltatime = 0
    start_x = 0

    if game_mode == 1:
        Levels = [modules.Modules.c]#, modules.Modules.cheat]
        Levels2 = [modules.Modules.c]#, modules.Modules.cheat]

        Level_coords = []

        for i in range(5):
            Levels.append(random.choice(modules.Modules.Levels))
            Levels2.append(random.choice(modules.Modules.Levels))

    ##Falsch Eingerückt --> Einrückung überbrücken
    while mainloop:
            level_length = 0
            start_x2 = start_x
            #pygame.mouse.set_pos([display_width / 2, display_height / 2])
            #i3 = random.choice(["S", "G"])
            display_width = pygame.display.get_surface().get_width()
            display_height = pygame.display.get_surface().get_height()
            
            if cSec == time.strftime("%S"):
                FPScount += 1
            else:
                FPS = FPScount
                FPScount = 0
                cSec = time.strftime("%S")
                if FPS > 0:
                    deltatime = 1 / FPS

            if Figur.y < 0:
                move_length = 32
                #Figur.y += 5 * Size
            else:
                move_length = Size / 8
                
            SpielFeld.fill(SCHWARZ)
            #SpielFeld.blit(Tiles.Sonne, (
            #    display_width - Size * 2, Size * 2))
            last_x = - Size
            ##Level rendering
            Boden = False
            Decke = False
            Links_Frei = True
            Rechts_Frei = True
            counter4 = 0
            #Levels2 = Levels
            #start_x = 0
            for Level in Levels2:
                #i3 = random.choice(["S", "G"])
                counter = 0
                counter2 = 0
                counter3 = 0
                counter4 += 1
                #counter3_end = 0
                for i in Level:
                    i2 = i
                    Fake = False
                    if i == "A":
                        i = "a"

                    if i == "?" or i == "ß":
                        liste = ["S", "G"]
                        i = "S"#random.choice(liste)
                        Levels[counter4 - 1].replace("?", i)
                        #pos = [counter3 - Size + 1, counter2 + 1]
                        
                    if i != "\n" and i != " " and i != "a":
                        #sys.stdout.write(str(i))
                        a = True
                        if i == "S" or i == "s":
                            surface = Tiles.Stein
                        elif i == "G" or i == "g":
                            surface = Tiles.Gras
                        elif i == "A":
                            surface 
                        #elif i == "?":
                        #    pass
                        else:
                            a = False

                        if (i2 == i.upper() and i2 != "ß") or i2 == "?":
                            Fake = False
                        else:
                            Fake = False
                        
                        if a:
                            x = (counter3 + 1) * Size + last_x + start_x2
                            y = (counter2 + 1) * Size #+ (
                                #display_height - (Size * 10)) + Size / 4 + 2
                            if i != "A":
                                x2 = abs(Figur.x + normal_x - x)
                                y2 = abs((Figur.y + Size) - y)
                                xy2 = (x2 + y2) / Size
                                if xy2 <= 11:
                                    if Figur.x <= display_width / 2:
                                        SpielFeld.blit(surface, (x, y))                                    
                                    else:
                                        SpielFeld.blit(surface, (
                                            x - Figur.x + display_width / 2, y))

                            

                            if (
                                Figur.x - move_length > x and
                                Figur.x - move_length < x + Size and
                                Figur.y + Size + move_length > y - Size and
                                Figur.y + Size + move_length < y + Size * 2 and
                                Fake == False
                                ):
                                Links_Frei = False

                            if (
                                Figur.x + move_length + Size > x and
                                Figur.x + move_length + Size < x + Size and
                                Figur.y + Size + move_length > y - Size and
                                Figur.y + Size + move_length < y + Size * 2 and
                                Fake == False
                                ):
                                Rechts_Frei = False

                            x2 = x
                            if Figur.Links and Links_Frei:
                                x2 += move_length

                            if Figur.Rechts and Rechts_Frei:
                                x2 -= move_length

                            if (
                                Figur.y + Size * 1 + move_length <= y and
                                Figur.y + Size * 2 + move_length >= y and
                                Figur.x > x2 - Size and
                                Figur.x < x2 + Size and
                                Fake == False
                                ):
                                Boden = True

                            if (
                                Figur.y + move_length - Size <= y and
                                Figur.y + move_length >= y and
                                Figur.x > x2 - Size and
                                Figur.x < x2 + Size and
                                Fake == False
                                ):
                                Decke = True
                            

                    if i == "a":
                        x = (counter3 + 1) * Size + last_x
                        #sys.stdout.write(" ")
                        
                    if i == "\n":
                        if counter != 0 and counter != len(modules.Modules.a):
                            #sys.stdout.write(5 * " " + str(counter2 + 1))
                            #print()
                            counter2 += 1
                            if not level_length:
                                level_length = counter3
                            counter_3 = counter3
                            counter3 = 0
                    if i != "\n" and i != " ":
                        counter3 += 1
                        
                    
                    counter += 1
                    
                    #pygame.display.update()

                        


                    for event in pygame.event.get():
                        if event.type == QUIT:
                            mainloop = False
                            mainloop2 = False

                        if event.type == KEYDOWN:
                            if not normal:
                                if event.key in Key.Keys["forward"]:
                                    Figur.Links = False
                                    Figur.Rechts = True
                                    Figur.Facing = "+"
                                    #Figur.x += 1

                                if event.key in Key.Keys["backward"]:
                                    Figur.Links = True
                                    Figur.Rechts  = False
                                    Figur.Facing = "-"
                                    #Figur.x -= 1

                                if (event.key in Key.Keys["jump"]) and Figur.can_jump == True:
                                    Figur.jumping = True
                                    Figur.can_jump = False

                                if event.key == pygame.K_KP0:
                                    Textures.next()

                            if event.key == pygame.K_RSHIFT:
                                if Musik_thread.activated:
                                    Musik_thread.activated = False
                                else:
                                    Musik_thread.activated = True

                            if event.key == pygame.K_RETURN:
                                if HitBox_showing:
                                    HitBox_showing = False
                                    Borders_active = False
                                    Circle_Hitbox = False
                                else:
                                    HitBox_showing = True
                                    Borders_active = True
                                    Circle_Hitbox = True

                            if event.key == pygame.K_KP_PLUS:
                                Musik_thread.next = True

                            if event.key == pygame.K_KP_MULTIPLY:
                                if Animation_thread.sound:
                                    Animation_thread.sound = False
                                else:
                                    Animation_thread.sound = True

                        if event.type == KEYUP:
                            if event.key in Key.Keys["forward"]:
                                #Figur.Links = False
                                Figur.Rechts = False

                            if event.key in Key.Keys["backward"]:
                                Figur.Links = False
                                #Figur.Rechts = False

                        #if event.type == MOUSEBUTTONDOWN:
                        #    print(event.pos[0], event.pos[1])

                        x_block = round(Figur.x / Size) + 1
                        if x_block > Score:
                            Score = x_block

                    
                #if game_mode == 1:
                #    if len(Level_coords) != len(Levels):
                #        if len(Level_coords) == counter4:
                #            Level_coords.append(x / Size)

                #if game_mode == 1:
                #    if len(Levels2) >= 10:
                #        Levels2.pop[0]
                #        start_x += 11

                

                #if x + Size * 100 < Figur.x:
                #    a = Levels2.pop((counter4 - 1))
                #    start_x += counter_3 * Size
                            
                last_x = x
                if Borders_active == True and abs(x - Figur.x) <= 11 * Size:
                    if Figur.x <= display_width / 2:
                        pygame.draw.line(SpielFeld, RED, (x + Size, Size),
                                         (x + Size, Size * 9 - move_length))
                    else:
                        x2 = x - Figur.x + display_width / 2 + Size
                        pygame.draw.line(SpielFeld, RED, (x2, Size),
                                         (x2, Size * 9 - move_length))

                start_x2 = 0

            
                
            if x - 50 * Size < Figur.x and game_mode == 1:
                Levels.append(random.choice(modules.Modules.Levels))
                Levels2.append(random.choice(modules.Modules.Levels))
                a = Levels2.pop(0)
                start_x += level_length * Size
    
            elif int(Figur.x / Size) >= 50 and game_mode == 2:
                if normal_x >= display_width / 2:
                    mainloop = False
                else:
                    normal = True
                    Borders_active = False
                    Figur.Rechts = False
                    normal_x += move_length
                

            if Figur.Links == True:
                if Figur.x - move_length >= 0 and Links_Frei:
                    Figur.x -= move_length

            elif Figur.Rechts == True:
                if Rechts_Frei:
                    Figur.x += move_length

            if ((Figur.Rechts and Rechts_Frei) or
                (Figur.Links and Links_Frei) or
                normal):
                    Figur.running = True

            else:
                Figur.running = False

            if Figur.jumping == True:
                Figur.max_jump_timer = 2 / move_length * 8
                if (
                    Figur.jump_timer <= Figur.max_jump_timer
                    ):
                    if (
                        1 == 1#int((Figur.jump_timer * 10) % move_length) == 0 #or
                        #int((Figur.jump_timer * 10) % move_length) == 1
                        ):
                        if not Decke:
                            Figur.y -= move_length
                        else:
                            Figur.jumping = False
                            Figur.jump_timer = 0
                            

                    Figur.jump_timer += 0.1

                else:
                    Figur.jump_timer = 0.1
                    Figur.jumping = False


            
            '''last_x = - Size
            counter4 = 0
            Boden = False
            Decke = False
            for Level in Levels:
                counter = 0
                counter2 = 0
                counter3 = 0
                counter4 += 1
                
                for i in Level:
                    i2 = i
                    Fake = False

                    if i == "?" or i == "ß":
                        liste = ["S", "G"]
                        i = random.choice(liste)
                        Levels[counter4 - 1].replace("?", i)
                        #pos = [counter3 - Size + 1, counter2 + 1]
                        
                    if i != "\n" and i != " " and i != "a":
                        #sys.stdout.write(str(i))
                        a = True
                        if i == "S" or i == "s":
                            surface = Tiles.Stein
                        elif i == "G" or i == "g":
                            surface = Tiles.Gras
                        elif i == "A":
                            surface 
                        #elif i == "?":
                        #    pass
                        else:
                            a = False

                        if (i2 == i.upper() and i2 != "ß") or i2 == "?":
                            Fake = False
                        else:
                            Fake = True
                        
                        if a:
                            x = (counter3 + 1) * Size + last_x
                            y = (counter2 + 1) * Size #+ (
                                #display_height - (Size * 10)) + Size / 4 + 2
                            if i != "A":
                                if Figur.x <= display_width / 2:
                                    SpielFeld.blit(surface, (x, y))
                                else:
                                    SpielFeld.blit(surface, (x - Figur.x + display_width / 2, y))

                            if (
                                Figur.y + Size * 1 + move_length <= y and
                                Figur.y + Size * 2 + move_length >= y and
                                Figur.x > x - Size and
                                Figur.x < x + Size and
                                Fake == False
                                ):
                                Boden = True

                            if (
                                Figur.y + move_length - Size <= y and
                                Figur.y + move_length >= y and
                                Figur.x > x - Size and
                                Figur.x < x + Size and
                                Fake == False
                                ):
                                Decke = True
                            

                    if i == "a":
                        x = (counter3 + 1) * Size + last_x
                        #sys.stdout.write(" ")
                        
                    if i == "\n":
                        if counter != 0 and counter != len(modules.Modules.a):
                            #sys.stdout.write(5 * " " + str(counter2 + 1))
                            #print()
                            counter2 += 1
                            counter3 = 0
                    if i != "\n" and i != " ":
                        counter3 += 1

                    counter += 1'''
                        
                  
            if not Boden and not Figur.jumping:
                Figur.y += move_length
                #print("1")

            if not normal and normal_x < 0:
                normal_x += move_length

            if Boden:
                Figur.can_jump = True
            else:
                Figur.can_jump = False

            if Figur.y >= Size * 10 - move_length:
                mainloop = False
                if game_mode == 1:
                    lost = True
                else:
                    Tutorial_die = True

            
            surface = Animation_thread.Animation
            if Figur.Facing == "-":
                surface = pygame.transform.flip(surface, True, False)
                
            if Figur.x <= display_width / 2:
                Figur_x = Figur.x
            else:
                Figur_x = display_width / 2 + normal_x

            SpielFeld.blit(surface, (Figur_x, Figur.y + move_length))
            SpielFeld.blit(Animation_thread.Fackelschein, (
                  Figur_x + (
                    Size - Animation_thread.Fackelschein.get_width()
                    ) / 2, Figur.y -
                    Animation_thread.Fackelschein.get_height() / 2 + move_length))
            SpielFeld.blit(Tiles.Abdeckung, (
                 Figur_x - Size * 14.5, Figur.y - 15 * Size + move_length))
            if Circle_Hitbox:
                 pygame.draw.circle(SpielFeld, RED, (
                     int(Figur_x + Size / 2), int(
                        Figur.y + move_length)), 1)
                 pygame.draw.circle(SpielFeld, RED, (
                    int(Figur_x + Size / 2), int(
                        Figur.y + move_length)),
                        int(Animation_thread.Fackelschein.get_width() / 2), 1)
            
                
            #pygame.draw.circle(SpielFeld, RED, (Figur.x, Figur.y + move_length), 1)
            Figur_y = Figur.y + move_length
            if Figur.x <= display_width / 2:
                Figur_x = Figur.x
            else:
                Figur_x = display_width / 2 + normal_x
            if HitBox_showing == True:
                pygame.draw.line(
                    SpielFeld, RED, (Figur_x, Figur_y), (Figur_x + Size, Figur_y))
                
                pygame.draw.line(
                    SpielFeld, RED, (Figur_x, Figur_y), (Figur_x, Figur_y + Size * 2))
                
                pygame.draw.line(
                    SpielFeld, RED, (Figur_x, Figur_y + Size * 2),\
                    (Figur_x + Size, Figur_y + Size * 2))
                
                pygame.draw.line(
                    SpielFeld, RED, (Figur_x + Size, Figur_y),\
                    (Figur_x + Size, Figur_y + Size * 2))
                

            FPS_overlay = Font.render(str(FPS), True, RED)
            SpielFeld.blit(FPS_overlay, (0, 0))

            '''Coordinates = str("Coordinates in Pixels:   x: "\
                              + str(round(Figur.x)) + ", y: "\
                              + str(Size * 9 - round(Figur.y)))
            Coordinate_overlay = Font.render(str(Coordinates), True, (100, 20, 10))
            SpielFeld.blit(Coordinate_overlay, (0, 20))'''

            #Coordinates = str("Coordinates:   x: "\
            #                  + str(round(Figur.x / Size) + 1)\
            #                  + ", y: " + str( 9 - (round(Figur.y / Size) + 2)))
            Coordinates = str("Score: %s"\
                              % str(round(Figur.x / Size) + 1))
            Coordinate_overlay = Font.render(str(Coordinates), True, RED)
            SpielFeld.blit(Coordinate_overlay, (0, 20))

            if Animation_thread.sound:
                pass
            else:
                SpielFeld.blit(Tiles.Sound_Muted, (
                    display_width - Size, 0))

            if Musik_thread.activated:
                pass
            else:
                if not Animation_thread.sound:
                    height = int(Tiles.Sound_Muted.get_height())
                else:
                    height = 0
                SpielFeld.blit(Tiles.Music_Paused, (
                    display_width - Size, height))
            
            pygame.display.update()

            clock.tick(30)

    final_x = Score
    message = ("Your Score was %s!" % final_x)
    #highscore_txt = open("Highscore.txt", "r")
    #a = 0
    #for line in highscore_txt:
    #    if a == 0:
    #        highscore = line
    #    a += 1

    #if a == 0:
    #    highscore = 0
        
    #highscore_txt.close()

    rank = Write.write(final_x, "Name")
    if rank:
        message = message + (" (Rank %s)" % rank)

    """
    new_highscore = False
    
    
    if final_x > int(highscore):
        highscore_txt = highscore_txt = open("Highscore.txt", "w")
        highscore_txt.write(str(final_x))
        highscore_txt.close()
        new_highscore = True

        pygame.display.update()

        #for i in range(100):
        #    pygame.display.update()
        #    time.sleep(0.1)
    """

Musik_thread.running = False
pygame.quit()

ExecShell.stop()

#print()
#print("Das ? ist an Der Stelle:")
#print("x: " + str(pos[0]) + ", y: " + str(pos[1]))
        
