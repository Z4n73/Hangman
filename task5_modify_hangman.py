import random

def hangman():
    
    #cool spanish words! (there are so many more :D)
    words = ["quijotesco", "sabotaje", "amazona", "aquelarre", "escalofrios",
             "aparato", "consciente", "asertividad", "juego", "ahorcado"]
    random_number = random.randint(0, 4)
    word = words[random_number]
    
    wrong_guesses = 0
    stages = ["",
              "________       ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|  D  E  A  D  "
              ]
    
    remaining_letters = list(word)
    board = [" _ "] * len(word)
    win = False
    
    print("Welcome to The Hangman")

    while wrong_guesses < len(stages) - 1:
    
        print("\n")
        
        message = "Guess a letter: "
        char = input(message)

        if char in remaining_letters:
                #ver como mejorar este código para que si la letra
                #está en la palabra, pinte todas las ocurrencias de
                #esa letra en el tablero (board)
            cind = remaining_letters.index(char) #index function returns the index of de first ocurrence of a character in a list
            board[cind] = char #replace the underscore in the board list with the letter they guessed
            remaining_letters[cind] = '$'#replace the letter they guessed with a dolar sign, so it is no longer in the "remaining letters" list
            print("\nGood, your guess was correct, go again!")
        else:
            wrong_guesses += 1 
            print("\nWrong letter, try again!")

        print("\n" + "".join(board))

        e = wrong_guesses + 1
        print("\n".join(stages[0:e])) #slice the stages list to print the hangman at whatever stage the game is at, starting at index 0 to index wrong + 1

        if " _ " not in board:
            print("\nYou win!")
            print(" ".join(board))
            win = True
            break
        
    if not win:
            #print("\n".join(stages[0:e])) #not really necessary, we are printing the final stage of the hangman with the last wrong guess...
            print("\nYou lose! The word was '{}".format(word) + "'.")


hangman()
