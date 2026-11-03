# Import libraries:
from tkinter import *
import random

# Declare global variables:
deck_of_cards = []
no_cards_per_player = 6
player_1_hand = []
computer_hand = []
trump_card = []

def create_new_deck():
    
    # Create a suits and individual cards:
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    cards = [x for x in range (2,14)]

    # Create a full deck of cards:
    for one_suit in suits:
        for one_card in cards:
            if one_card == 11:
                tempcard = (f"Jack of {one_suit}")
            elif one_card == 12:
                tempcard = (f"Queen of {one_suit}")
            elif one_card == 13:
                tempcard = (f"King of {one_suit}")
            elif one_card == 12:
                tempcard = (f"Ace of {one_suit}")
            else:
                tempcard = (f"{one_card} of {one_suit}")
            deck_of_cards.append(tempcard)

    #print (deck_of_cards)

def deal_cards():

    for i in range(1,no_cards_per_player):

        # Pick a random card:
        one_card = random.choice(deck_of_cards)

        # Give the random card to the player:
        player_1_hand.append (one_card)
        deck_of_cards.remove (one_card)

        # Pick another random card:
        one_card = random.choice(deck_of_cards)

        # Give the random card to the computer deck:
        computer_hand.append (one_card)
        deck_of_cards.remove (one_card)

# Configure the outer screen:
root = Tk()
root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")
root.geometry("900x500")
root.configure(background="green")

# Create outer frame for the game:
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create frame for dealer cards:
dealer_frame = LabelFrame(my_frame, text="Dealer Hand",bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=40)

# Create frame for player cards:
player_frame = LabelFrame(my_frame, text="Your Hand",bd=0)
player_frame.grid(row=0, column=1, ipadx=40)

# Create a new deck of cards:
create_new_deck()

# Deal the cards to all players:
deal_cards()

print ("Player 1 hand")
print (player_1_hand)
print ("Computer hand")
print (computer_hand)

# Put cards in dealer frame:
dealer_label = Label(dealer_frame, text ="Test1")
dealer_label.pack(pady=50)

# Put cards in player frame:
player_label = Label(player_frame, text = "Test2")
player_label.pack(pady=50)

# Create button to shuffle the deck:
shuffle_button = Button(root, text="Shuffle the Deck")
shuffle_button.pack(pady=20)

# Create button to deal the cards:
deal_button = Button(root, text="Deal the Cards")
deal_button.pack(pady=20)


root.mainloop()

print ("Completed my run 2342342234")
