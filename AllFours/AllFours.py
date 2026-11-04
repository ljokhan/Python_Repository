###########################################################################################

# Import libraries:
from tkinter import *
from PIL import Image, ImageTk
import random


###########################################################################################

# Declare global variables:
deck_of_cards = []
no_cards_per_player = 3

# These set the size of the frames which holds the cards:
global frame_width
frame_width = 150

global frame_height
frame_height = 150

# These global variables hold the cards for each player and the trump card:
player_1_hand = []
computer_hand = []
trump_card = []

###########################################################################################

def configure_main_screen():

    # Configure the main screen:
    global root
    root = Tk()
    root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")
    root.geometry("1600x800")
    root.configure(background="green")

    #bg_image = Image.open("./bg.jpg")  # Supports PNG, JPG, etc.
    #bg_photo = ImageTk.PhotoImage(bg_image)
    #bg_label = Label(root, image=bg_photo)
    #bg_label.place(relwidth=1, relheight=1)
    # Keep a reference to prevent the image from being garbage collected
    # bg_label.image = bg_photo


###########################################################################################

def create_frames():

    # Create outer frame for the game:
    global my_frame 
    my_frame = Frame(root, bg="green")
    my_frame.pack(pady=20)

#

    # Create frame for trump card:
    global trump_frame
    trump_frame = LabelFrame(my_frame, width = frame_width, height = frame_height, text ="Trump Card",bd=0)
    trump_frame.grid(row=0, column=1, padx=20, ipadx=40, pady=20)

    # Create frame for dealer cards:
    global dealer_frame_card_1
    dealer_frame_card_1 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Dealer Hand",bd=0)
    dealer_frame_card_1.grid(row=1, column=0, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_2
    dealer_frame_card_2 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Dealer Hand",bd=0)
    dealer_frame_card_2.grid(row=1, column=1, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_3
    dealer_frame_card_3 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Dealer Hand",bd=0)
    dealer_frame_card_3.grid(row=1, column=2, padx=20, ipadx=40, pady=20)

    # Create frame to hold card 1 for each round:
    global round_frame_card_1
    round_frame_card_1 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Round Card 1",bd=0)    
    round_frame_card_1.grid(row=2, column=0, padx=20, ipadx=40, pady=20)

    # Create frame to hold card 2 for each round:
    global round_frame_card_2
    round_frame_card_2 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Round Card 2",bd=0)    
    round_frame_card_2.grid(row=2, column=1, padx=20, ipadx=40, pady=20)

    # Create frame for player cards:
    global player_frame_card_1
    player_frame_card_1 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Your Hand",bd=0)
    player_frame_card_1.grid(row=3, column=0, padx=20, ipadx=40, pady=20)

    global player_frame_card_2
    player_frame_card_2 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Your Hand",bd=0)
    player_frame_card_2.grid(row=3, column=1, padx=20, ipadx=40, pady=20)

    global player_frame_card_3
    player_frame_card_3 = LabelFrame(my_frame, width = frame_width, height = frame_height, text="Your Hand",bd=0)
    player_frame_card_3.grid(row=3, column=2, padx=20, ipadx=40, pady=20)

     # Initial population of all frames:
    global dealer_label
    dealer_label = Label(dealer_frame_card_1, text ="Dealer Card 1")
    dealer_label.grid_propagate()

    global dealer_label_2
    dealer_label_2 = Label(dealer_frame_card_2, text ="Dealer Card 2")
    dealer_label_2.grid_propagate(True)

    global dealer_label_3
    dealer_label_3 = Label(dealer_frame_card_3, text ="Dealer Card 3")
    dealer_label_3.grid_propagate(False)



    global round_frame_card1_label
    round_frame_card1_label = Label(round_frame_card_1, text = "Round Card 1")
    round_frame_card1_label.pack()

    global round_frame_card2_label
    round_frame_card2_label = Label(round_frame_card_2, text = "Round Card 2")
    round_frame_card2_label.pack_propagate(False)



    global player_label
    player_label = Label(player_frame_card_1, text = "Player Card 1")
    player_label.pack()

    global player_label_2
    player_label_2 = Label(player_frame_card_2, text = "Player Card 2")
    player_label_2.pack_propagate(False)

    global player_label_3
    player_label_3 = Label(player_frame_card_3, text = "Player Card 3")
    player_label_3.pack_propagate(False)

    global trump_label
    trump_label = Label(trump_frame, text = "Trump Card")
    trump_label.pack_propagate(False)

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

    trump_label.configure(text = "ccc")

    dealer_label.configure(text = computer_hand[0])
    dealer_label_2.configure(text = computer_hand[1])
    dealer_label_3.configure(text = computer_hand[2])
    
    player_label.configure(text = player_1_hand[0])
    player_label_2.configure(text = player_1_hand[1])
    player_label_3.configure(text = player_1_hand[2])

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
