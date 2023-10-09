import random
import json

jsonFile = "GreatArcana.json"


def _run(draws):

    def read_Json(file,):
        #opens and reads the file to the data var
        def read_json():
            with open(file) as f:
                data = json.load(f)
                return data
        #split the neccesary paths for easier access into global var
        def split_json(data):
            #assign global var because im lazy af
            global AllArcana
            AllArcana = data["GreatArcana"]
        _data=read_json()
        split_json(_data)
    def grab_Keys_From_Json():
        _Arcana = []
        for Arc in AllArcana[0]:
            _Arcana.append(Arc) #get all keys in the json
        return _Arcana

    #read json
    read_Json(jsonFile)
    #get all the arcana names
    Arcana = grab_Keys_From_Json()



    #get x random arcana where X is the number of draws
    _selected_Arcana = random.sample(Arcana, draws)

    for selected in _selected_Arcana:
        
        rand_pos= random.randint(0, 1) #generate a random position 0=upright, 1=reversed
        print("Card: "+ selected)
        #check if the Arcana is reversed or upright and print that for better user experience
        if rand_pos == 1:
            print("Position: Reversed")
        else:
            print("Position: Upright")
        #print the meaning of the Arcana and the selected position
        print("Meaning: " + AllArcana[0][Arcana[_selected_Arcana.index(selected)]][rand_pos])
        print("\n")
