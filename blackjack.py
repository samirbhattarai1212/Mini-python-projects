
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


import random
import os
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
     return "Draw 🙃"
    elif computer_score == 0:
     return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
     return "Win with a Blackjack 😎"
    elif user_score > 21:
     return "You went over. You lose 😭"
    elif computer_score > 21:
     return "Opponent went over. You win 😁"
    elif user_score > computer_score:
     return "You win 😃"
    else:
     return "You lose 😤"
    
def play():
    user_cards=[]
    computer_cards=[]
    game_end= False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_end:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards: {user_cards} and your score: {(user_score)}")
        print(f"computer first card:{computer_cards[0]}")

        if computer_score==0 or user_score==0 or user_score>21:
            game_end=True
        else:
            user_choice=input("Type 'y' for another card and 'n' to end game.")
            if user_choice=="y":
                user_cards.append(deal_card())
            else:
                game_end=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"your final hand {user_cards} and final score is {user_score}")
    print(f"computer final hand {computer_cards} and final score is {computer_score}")
    print(compare(user_score,computer_score))

gameplay= input("DO you want to play blackjack game? type 'y' to continue: ")
if gameplay =="y":
    play()
    
     
      




