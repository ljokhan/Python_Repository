###########################################################################################

# Import libraries:
from tkinter import *
from PIL import Image, ImageTk
import random

###########################################################################################

# Declare global variables:
deck_of_cards = []
no_cards_per_player = 3
player_1_hand = []
computer_hand = []
trump_card = []

###########################################################################################

def configure_main_screen():

    # Configure the main screen:
    global root
    root = Tk()
    root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")
    root.geometry("1200x500")
    root.configure(background="green")

###########################################################################################

def create_frames():

    # Create outer frame for the game:
    global my_frame 
    my_frame = Frame(root, bg="green")
    my_frame.pack(pady=20)

    # Create frame for trump card:
    global trump_frame
    trump_frame = LabelFrame(my_frame, text ="Trump Card",bd=0)
    trump_frame.grid(row=0, column=0, padx=20, ipadx=40)

    # Create frame for dealer cards:
    global dealer_frame_card_1
    dealer_frame_card_1 = LabelFrame(my_frame, text="Dealer Hand",bd=0)
    dealer_frame_card_1.grid(row=1, column=0, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_2
    dealer_frame_card_2 = LabelFrame(my_frame, text="Dealer Hand",bd=0)
    dealer_frame_card_2.grid(row=1, column=1, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_3
    dealer_frame_card_3 = LabelFrame(my_frame, text="Dealer Hand",bd=0)
    dealer_frame_card_3.grid(row=1, column=2, padx=20, ipadx=40, pady=20)

    # Create frame for player cards:
    global player_frame_card_1
    player_frame_card_1 = LabelFrame(my_frame, text="Your Hand",bd=0)
    player_frame_card_1.grid(row=2, column=0, ipadx=40, pady=20)

    global player_frame_card_2
    player_frame_card_2 = LabelFrame(my_frame, text="Your Hand",bd=0)
    player_frame_card_2.grid(row=2, column=1, ipadx=40, pady=20)

    global player_frame_card_3
    player_frame_card_3 = LabelFrame(my_frame, text="Your Hand",bd=0)
    player_frame_card_3.grid(row=2, column=2, ipadx=40, pady=20)

      # Initial population of all frames:
    global dealer_label
    dealer_label = Label(dealer_frame_card_1, text ="Dealer Card 1")
    dealer_label.pack(pady=30)

    global dealer_label_2
    dealer_label_2 = Label(dealer_frame_card_2, text ="Dealer Card 2")
    dealer_label_2.pack(pady=30)

    global dealer_label_3
    dealer_label_3 = Label(dealer_frame_card_3, text ="Dealer Card 3")
    dealer_label_3.pack(pady=30)

    global player_label
    player_label = Label(player_frame_card_1, text = "Player Card 1")
    player_label.pack(pady=30)

    global player_label2
    player_label2 = Label(player_frame_card_2, text = "Player Card 2")
    player_label2.pack(pady=30)

    global player_label3
    player_label3 = Label(player_frame_card_3, text = "Player Card 3")
    player_label3.pack(pady=30)

    global trump_label
    trump_label = Label(trump_frame, text = "Trump Card")
    trump_label.pack(pady=30)

###########################################################################################

def resize_card(card_image):
    pass

###########################################################################################

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

###########################################################################################

def deal_cards():

    for i in range(1, 1 + no_cards_per_player):

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

###########################################################################################

def kick_trump_card():
    # Pick a random card:
    one_card = random.choice(deck_of_cards)

    # Give the random card to the trump card:
    trump_card.append (one_card)
    deck_of_cards.remove (one_card)

###########################################################################################

def create_buttons(root):

    # Create button to shuffle the deck:
    shuffle_button = Button(root, text="Shuffle the Deck")
    shuffle_button.pack(pady=20)

    # Create button to deal the cards:
    deal_button = Button(root, text="Deal the Cards")
    deal_button.pack(pady=20)

###########################################################################################

def put_cards_in_frames(dealer_label, player_label, trump_label):

    trump_label.configure(text = trump_card[0])

    dealer_label.configure(text = computer_hand[0])
    dealer_label_2.configure(text = computer_hand[1])
    dealer_label_3.configure(text = computer_hand[2])
    

    player_label.configure(text = player_1_hand[0])
    

###########################################################################################

# Configure the main screen:
configure_main_screen()

# Create the frames for the game:
create_frames()

# Create buttons for the game:
create_buttons(root)

# Create a new deck of cards:
create_new_deck()

# Deal the cards to all players:
deal_cards()

print ("Player 1 hand")
print (player_1_hand)
print ("Computer hand")
print (computer_hand)

# Kick the trump card:
kick_trump_card()

print ("Trump card")
print (trump_card)

# Place cards in the frames:
put_cards_in_frames(dealer_label, player_label, trump_label)


root.mainloop()

print ("Completed my run 2342342234")
