import json, os

def LoadLevel(Level = 1):
        Level -= 1
        with open(os.path.abspath(".") + r"\levels.txt") as file:
                data = json.load(file); file.close()
	
        for i in data["levels"]:
                a = ""
                for j in i["Map"]:
                        string = ""
                        if a != "":
                                string = "\n"
                        string += j
                        a += string
                i["Map"] = a
		
        x_len = len(data["levels"][Level]["Map"].split("\n")[0])
        y_len = data["levels"][Level]["Map"].count("\n") + 1
	
        print()
        print(data["levels"][Level]["Map"])
        print()
	#for j in range(x_len * 2):
	#	print("-", end = "")
        for i in range(y_len):
                for j in range(x_len):
                        p = False
                        for t in data["levels"][Level]["Tags"]:
                                if t["type"] == "Lever":
                                        if [j + 1, i + 1] == t["c1"]:
                                                print("L", end = "")
                                                p = True
                                elif t["type"] == "Pressure_Plate":
                                        if [j + 1, i + 1] == t["c1"]:
                                                print("P", end = "")
                                                p = True
                                elif t["type"] == "Door":
                                        if ([j + 1, i + 1] == t["c"] or
                                            [j + 1, i + 2] == t["c"]):
                                                print("D", end = "")
                                                p = True
                        if not p:
                                print("-", end = "")
                print()
	#for j in range(x_len * 2):
	#	print("-", end = "")

if __name__ == "__main__":
    LoadLevel()
