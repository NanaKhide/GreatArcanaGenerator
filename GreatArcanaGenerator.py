import random
import json

jsonFile = "GreatArcana.json"
draws = 3

def handle_json(file,):
    #opens and reads the file to the data var
    def read_json():
        with open(file) as f:
            global data
            data = json.load(f)
    #split the neccesary paths for easier access into global var
    def split_json():
        global AllArcana
        AllArcana = data["GreatArcana"]
    read_json()
    split_json()

#read json
handle_json(jsonFile)

Arcana = []
for Arc in AllArcana[0]:
    Arcana.append(Arc) #get all keys in the json
max_rand = len(Arcana)-1 #get the length of the json
while draws > 0: #draw x amount of times where x is draw var
    print("\n")
    rand_key= random.randint(0, max_rand) #generate a random number for the arcana
    rand_pos= random.randint(0, 1) #generate a random position 0=upright, 1=reversed

    #print(rand_key, rand_pos)  ----debug----
    _key = Arcana[rand_key] #get the name of the key to search for in the array
    print("Card: "+_key)
    if rand_pos == 1:
        print("Position: Reversed")
    else:
        print("Position: Upright")
    print("Meaning: " + AllArcana[0][Arcana[rand_key]][rand_pos])
    
    draws = draws - 1
print("\n")
input()#forces the terminal to stay open, remove if you dont want that
