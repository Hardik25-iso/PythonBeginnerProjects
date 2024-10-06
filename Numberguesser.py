def numberguesser():


    import random

    print("Hi! Welcome to the game.This is a number guessing game.\nWhere you get 7 chances to get the correct number.\nLet's Start the game")

    number_guess = random.randrange(50)
    chances = 7
    guess = 0
    while guess < chances:
        
        guess +=1

        my_guess = int(input("Enter your number:"))

        if my_guess == number_guess:
            print(f"Congrats!! {my_guess} is the correcct answer.You completed the game in {guess} chances.")
        
            break 

        elif chances == guess and number_guess != my_guess:
            print(f"Better Luck next time ,The number was {number_guess}")
    

        elif my_guess > number_guess:
            print("Oh no You guessed a little high,Try again")

        elif my_guess < number_guess:
            print("Oh no you guessed a little low,Try again")     

numberguesser()
