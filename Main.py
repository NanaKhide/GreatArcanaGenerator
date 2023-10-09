import GreatArcanaGenerator

default_number_of_cards = 3

print("⁜  ⁜ Arcana Generator main  ⁜ ⁜ \n")
while True:
    print("The current default number of cards is: ", default_number_of_cards)
    try:
        number_of_cards = int(input("Please Input the amount of Cards you wish to draw from the Deck or press enter to use the Default\n")or default_number_of_cards)
        GreatArcanaGenerator._run(number_of_cards)

    except Exception as e:
        print("Your input didnt match the requirements. Error:", e, "\n")