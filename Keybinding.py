import pygame
from pygame.locals import *
import os
import json
import copy

pygame.init()
path = str(os.path.abspath(".") + r"\Keybindings.txt")

def int_to_key(number):
    key = pygame.key.name(number)
    return key

def key_to_int(key):
    #number = eval("pygame.locals.K_" + key)
    try:
        number = eval("pygame.locals.K_" + key.title())
    except:
        try:
            number = eval("pygame.locals.K_" + key.lower())
        except:
            try:
                number = eval("pygame.locals.K_" + key.upper())
            except:
                pass
    return number

def test_print():
    print("Keys_now: " + str(Key.Keys_now), "\nKeys:     " + str(Key.Keys) +
          "\n" + str(Key.Keys_now == Key.Keys))

def create_data(path):
    data = {"keys": [{"name":"forward", "key":["d", "RIGHT"]},
                     {"name":"jump", "key":["w","UP"]},
                     {"name":"backward", "key":["a", "LEFT"]}]}
            
    with open(path, "w") as file:
        json.dump(data, file, indent = 4); file.close()
    

def load_data(path):
    if "Keybindings.txt" not in os.listdir():
        with open(path, "w+") as file:
            file.write("")
            file.close()
    try:
        with open(path, "r") as file:
            data = json.load(file); file.close()
        return data
    except json.JSONDecodeError:
        create_data(path)
        

def data_to_dict(data):
    data = load_data(path)
    if not "keys" in data:
        create_data(path)
    else:
        for i in data["keys"]:
            Key.Keys[i["name"]] = i["key"]
            for j in range(len(i["key"])):
                i["key"][j] = key_to_int(str(i["key"][j]))
                

def update_keys():
    Key.Keys = copy.deepcopy(Key.Keys_now)
    data = json.loads('{"keys": []}')
    for i in ["forward", "backward", "jump"]:
        a = Key.Keys[i]
        data["keys"].append({})
        data["keys"][-1]["name"] = i
        data["keys"][-1]["key"] = a
        for j in range(len(data["keys"][-1]["key"])):
            data["keys"][-1]["key"][j] = int_to_key(data["keys"][-1]["key"][j])
    Key.Keys = copy.deepcopy(Key.Keys_now)
            
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)
        file.close()
        

Original_Keys = {
    "forward" :  [key_to_int("d"), key_to_int("RIGHT")],
    "backward" : [key_to_int("a"), key_to_int("LEFT") ],
    "jump" :     [key_to_int("w"), key_to_int("UP")   ]}

#Keys = copy.deepcopy(Original_Keys)

#Keys = Original_Keys()

class Key:
    Keys = copy.deepcopy(Original_Keys)

if __name__ == "__main__":
    data_to_dict(load_data(path))
    Key.Keys_now = copy.deepcopy(Key.Keys)
