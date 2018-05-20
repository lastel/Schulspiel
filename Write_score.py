import json
import os
path = str(os.path.abspath(".") + "\\scores.txt")

class Write:
    def write(score, name):
        if "scores.txt" not in os.listdir():
            with open(path, "w+") as file:
                file.write("")
                file.close()
        try:
        #if 1 == 1:
            with open(path, "r") as file:
                data = json.load(file); file.close()
            counter = 0
            inserted = False
            place = False
            for i in data["scores"]:
                #print(i)
                #print(data["scores"][i]["score"])
                if score > data["scores"][counter]["score"]:
                    data["scores"].insert(counter, {})
                    data["scores"][counter]["name"] = name
                    data["scores"][counter]["score"] = int(score)
                    inserted = True
                    place = counter + 1
                    break
                counter += 1
            while len(data["scores"]) > 10:
                del data["scores"][-1]
            if len(data["scores"]) < 10 and not inserted:
                data["scores"].insert(counter, {})
                data["scores"][counter]["name"] = name
                data["scores"][counter]["score"] = int(score)
                place = len(data["scores"])
            with open(path, "w") as file:
                json.dump(data, file, indent = 4); file.close()
            return place
        
        except json.JSONDecodeError:
            data = {"scores": [{"name":name, "score":score}]}
            with open(path, "w") as file:
                json.dump(data, file, indent = 4); file.close()
            place = 1
            return place
        #except:
        #    pass
        
class Ausgabe:
    def ausgabe():
        with open(path) as file:
            data = json.load(file); file.close()
        for i in data["scores"]:
            print(i["name"] + ":", i["score"], "Punkte!")


class Scores:
    def highscore():
        with open(path, "r") as file:
            data = json.load(file); file.close()
        score = data["scores"][0]["score"]
        return score
