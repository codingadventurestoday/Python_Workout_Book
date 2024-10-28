import random as ran

def guessing_game():
    """Gather user's guess for int until the number is guessed correctly
       provides user with feedback about their guess to actual"""
    number_to_guess = ran.randint(1, 100)

    predicted = False
    while predicted == False:
        user_input = input("Please guess a number between 1 and 100: ")
        try: 
            guessed_number = int(user_input)
        except ValueError:
            print("You have entered a value that is not a whole number")
        
        if guessed_number == number_to_guess:
            print(f"Woah you guess the correct number of {number_to_guess}")
            predicted = True
            break 

        elif guessed_number > number_to_guess:
            print("Your guess was too high. Try a lower number")
        else:
            print("Your guess was too low. Try a higher number")


guessing_game()