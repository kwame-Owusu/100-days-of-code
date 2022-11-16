import os
from blindacution_art import logo


print(logo)

print("Welcome to the blind auction program")

bids = {}
bidding_finished = False

# defining who is the highest bidder, and whoever is the higest wins
def highest_bidder(bidding_record):
    top_bid = 0
    winner = ""
    for bidder in bidding_record:
       bid_amount= bidding_record[bidder]
       if bid_amount > top_bid:
        top_bid = bid_amount
        winner = bidder
    print(f"The winner is {winner} with a bid of ${top_bid}")



while not bidding_finished:
    name = input("What is your name?: \n")
                
    bid_price=  int(input("What's your bid?: \n"))

    # putting the name as the 'key' and the bid_price as the 'value' this will change depending on the user name and bidding price.
    bids[name] = bid_price
                
    restart_auction = input("Are there any other bidders? Type 'yes' or 'no'.")

    if restart_auction == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif restart_auction =="yes":
        os.system('cls')

        


    
    
                    
  
 





















