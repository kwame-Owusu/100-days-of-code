from guess_art import logo,goodbye
import random
import os



# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)

print("Welcome to the guessing game!")
def guess_game():
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
    print(difficulty)
    
    
    # if the difficulty chosen by user is == to 'easy' then user has 10 changes if difficulty == 'hard' user has 5 chances.
    if difficulty == "easy":
        print("You have 10 chances")
        for x in range(10):
            user_guess = int(input("Guess a number between 1 and 100: \n"))

            random_guess= random.randint(0,101)
            
            if user_guess ==  random_guess:
                print(f"You've guessed correctly {random_guess}")
           
                 
            elif user_guess < random_guess:
                print("Too low")
            elif user_guess > random_guess:
                print("too high")
        

    

    if difficulty == "hard":
        print("You have 5 chances")
        for x in range(5):
            user_guess = int(input("Guess a number between 1 and 100: \n"))

            random_guess= random.randint(0,101)
                
            if user_guess ==  random_guess:
                    print(f"You've guessed correctly {random_guess}")
            
                    
            elif user_guess < random_guess:
                    print("Too low")
            elif user_guess > random_guess:
                    print("too high")
                    

guess_game()

# prompt for a restart or quit the game.
restart_game = input("Would like to replay the game? Type 'y' or 'n \n").lower()
if restart_game == "y":
        guess_game()
        os.system('cls')
elif restart_game == "n":
    print("goodbye")

    


    
        


