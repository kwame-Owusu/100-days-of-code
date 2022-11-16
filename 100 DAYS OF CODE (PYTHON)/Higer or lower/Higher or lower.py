

import os
from game_data import data
from game_art import logo,vs
import random


def dict_dissapear(data):
    """making the dictionary brackets dissapear and change it into string without the folower_count"""
    name = data["name"]
    description =  data["description"]
    country = data["country"]
    return  f"{name}, a {description}, from {country}"



def check_answer(guess,follower_count1,follower_count2):
    """check if follower_count1(which is follower count of random_celeb1) is bigger than follower_count2(follower count of random_celeb2)"""
    if follower_count1 > follower_count2:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    random_celeb1 = random.choice(data) 
    random_celeb2 = random.choice(data) 
    # follower_count1= random_celeb1['follower_count']
    # follower_count2= random_celeb2['follower_count']

    
    score = 0
    game_continue = True


    while game_continue:
        """ to continue the game as long as the answer is correct"""
        random_celeb1 = random_celeb2
        random_celeb2 = random.choice(data)
        while random_celeb1 == random_celeb2:
            random_celeb2 == random.choice(data)
        
        print(f"Compare A: {dict_dissapear(random_celeb1)}")
        print(vs)
        print(f"Against B: {dict_dissapear(random_celeb2)}")
        guess = input("Who has more followers, Type 'A' or 'B'? ").lower()
        follower_count1= random_celeb1['follower_count']
        follower_count2= random_celeb2['follower_count']
        is_correct = check_answer(guess,follower_count1,follower_count2)
        
        os.system('cls')
        print(logo)
        if is_correct:
            score += 1
        else:
            game_continue = False
            print(f"Sorry, thats wrong.\n Final score: {score}")
        
        
game()

