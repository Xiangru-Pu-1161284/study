#This program is a guessing game. You can guess the fictional character by inputting the name, or you can type 'hint' for some help. You will receive a response when you do it right or wrong.
print("Welcome to the fictional character guessing game.\n")
print("I'm thinking of a female character from a children's story, have a guess who I am thinking of.")

guessed = False
hint_counter = 0
while not guessed:
    name_guessed = input("Enter your guess or hint if you need some help: ")
    if (name_guessed.lower().strip() == 'hint'):
        hint_counter +=1
        if hint_counter == 1:
            print("Queen\n")
        elif hint_counter==2:
            print("Magic mirror\n")
        elif hint_counter==3:   
            print("Huntsman\n")
        elif hint_counter ==4:
            print("Seven dwarfs\n")
        else:
            print("Sorry that is all my hints!")
    else:
        if len(name_guessed) < 10:
            print("I'm thinking of a longer name\n")
        elif len(name_guessed)> 10:
            print("That name is too long\n")
        else:
            if name_guessed.lower().strip()=='snow white':
                guessed = True
                print("Well Done, you guessed what I was thinking of, just right!")
            else:
                print("That name is the right length, but isn't the one I'm thinking of")