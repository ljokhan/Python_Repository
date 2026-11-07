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
frame_width = 80

global frame_height
frame_height = 150

# These global variables hold the cards for each player and the trump card:
player_1_hand = []
computer_hand = []
trump_card = []

###########################################################################################

def create_application():

    # Create the main application window:
    global root
    root = Tk()
    root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")

    # Configure background color:
    root.configure(background="green")

    # Enable fullscreen mode:
    #root.attributes('-fullscreen', True)
    root.geometry("1200x800")
    
    # Bind the Escape key to exit fullscreen mode:
    #root.bind('<Escape>', exit_fullscreen)

    #bg_image = Image.open("./bg.jpg")  # Supports PNG, JPG, etc.
    #bg_photo = ImageTk.PhotoImage(bg_image)
    #bg_label = Label(root, image=bg_photo)
    #bg_label.place(relwidth=1, relheight=1)
    # Keep a reference to prevent the image from being garbage collected
    # bg_label.image = bg_photo


#root = Tk()
#--root.geometry("400x300")

#--root.rowconfigure(0, weight=1)
#--root.columnconfigure(0, weight=1)
#--root.columnconfigure(1, weight=3)

#--left_sidebar = Frame(root, bg="green")
#--left_sidebar.grid(row = 0, column=0, sticky="nsew")

#--main_content = Frame(root, bg="blue")
#--main_content.grid(row = 0 , column =1, sticky="nsew")

###########################################################################################

def exit_fullscreen(event=None):

    # Toggle off fullscreen or close the application
    root.attributes('-fullscreen', False)

     # Uncomment to close the app entirely:
    ########root.destroy() 
    # 

###########################################################################################

def create_frames():

    # Split main application window into (1) side-bar to display points and (2) main board where cards are played
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)    
    root.columnconfigure(1, weight=3)

    # Create frame for side-bar:
    global frame_left_sidebar
    frame_left_sidebar = Frame(root, bg="yellow")
    frame_left_sidebar.grid(row = 0, column=0, sticky="nsew")

    # Create frame where cards are played
    global frame_main_board
    frame_main_board = Frame(root, bg="#3ce663", bd=2)
    frame_main_board.grid(row = 0, column=1, sticky="nsew")

    # Create frame for trump card:
    global trump_frame
    trump_frame = LabelFrame(frame_main_board, width = frame_width, height = frame_height, bd=0, text="Trump Card frame")
    trump_frame.grid(row=0, column=1, padx=20, ipadx=40, pady=20)

    global trump_label
    trump_label = Label(trump_frame, text='1. This is a Label.')
    trump_label.place(x=0, y=5)

    # Create frame for dealer cards:
    global dealer_frame_card_1
    dealer_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Dealer Hand frame 1",bd=0)
    dealer_frame_card_1.grid(row=1, column=0, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_1_label
    dealer_frame_card_1_label = Label(dealer_frame_card_1, text='1. This is a Label.')
    dealer_frame_card_1_label.place(x=0, y=5)

    global dealer_frame_card_2
    dealer_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Dealer Hand frame 2",bd=0)
    dealer_frame_card_2.grid(row=1, column=1    , padx=20, ipadx=40, pady=20)

    global dealer_frame_card_2_label
    dealer_frame_card_2_label = Label(dealer_frame_card_2, text='1. This is a Label.')
    dealer_frame_card_2_label.place(x=0, y=5)

    global dealer_frame_card_3
    dealer_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Dealer Hand frame 3",bd=0)
    dealer_frame_card_3.grid(row=1, column=2, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_3_label
    dealer_frame_card_3_label = Label(dealer_frame_card_3, text='1. This is a Label.')
    dealer_frame_card_3_label.place(x=0, y=5)

    ##########################################################################################################################
    # Create frames to hold cards for each round:
    ##########################################################################################################################

    global round_frame_card_1
    round_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Round Card frame 1",bd=0)    
    round_frame_card_1.grid(row=2, column=0, padx=20, ipadx=40, pady=20)

    global round_frame_card_1_label   
    round_frame_card_1_label = Label(round_frame_card_1, text='')
    round_frame_card_1_label.place(x=0, y=5)

    # reate frame to hold card 2 for each round:
    global round_frame_card_2
    round_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Round Card frame 2",bd=0)    
    round_frame_card_2.grid(row=2, column=1, padx=20, ipadx=40, pady=20)

    global round_frame_card_2_label
    round_frame_card_2_label = Label(round_frame_card_2, text='')
    round_frame_card_2_label.place(x=0, y=5)

    ##########################################################################################################################
    # Create clickable frames for player cards:
    ##########################################################################################################################

    global player_frame_card_1
    player_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Your Hand frame 3",bd=0)
    player_frame_card_1.grid(row=3, column=0, padx=20, ipadx=40, pady=20)
    player_frame_card_1.bind("<Button-1>", player_frame_card_1_click)

    global player_frame_card_1_label
    player_frame_card_1_label = Label(player_frame_card_1, text='1. This is a Label.')
    player_frame_card_1_label.place(x=0, y=5)

    global player_frame_card_2
    player_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Your Hand frame 2",bd=0)
    player_frame_card_2.grid(row=3, column=1, padx=20, ipadx=40, pady=20)
    player_frame_card_2.bind("<Button-1>", player_frame_card_2_click)

    global player_frame_card_2_label
    player_frame_card_2_label = Label(player_frame_card_2, text='1. This is a Label.')
    player_frame_card_2_label.place(x=0, y=5)

    global player_frame_card_3
    player_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="Your Hand frame 3",bd=0)
    player_frame_card_3.grid(row=3, column=2, padx=20, ipadx=40, pady=20)
    player_frame_card_3.bind("<Button-1>", player_frame_card_3_click)

    global player_frame_card_3_label
    player_frame_card_3_label = Label(player_frame_card_3, text='1. This is a Label.')
    player_frame_card_3_label.place(x=0, y=5)

###########################################################################################

def player_frame_card_1_click (event):

    print("Frame was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    round_frame_card_1_label.configure(text = player_1_hand[0]) 
    player_frame_card_1_label.configure(text = "PLAYED CARD") 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    round_frame_card_2_label.configure(text = computer_hand[0])

    #dermine_round_winner()

###########################################################################################

def player_frame_card_2_click (event):

    print("Frame was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    round_frame_card_1_label.configure(text = player_1_hand[1]) 
    player_frame_card_2_label.configure(text = "PLAYED CARD") 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    round_frame_card_2_label.configure(text = computer_hand[1])

    determine_round_winner()

###########################################################################################

def player_frame_card_3_click (event):

    print("Frame was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    round_frame_card_1_label.configure(text = player_1_hand[2]) 
    player_frame_card_3_label.configure(text = "PLAYED CARD") 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    round_frame_card_2_label.configure(text = computer_hand[2])

    determine_round_winner()

###########################################################################################

def determine_round_winner():
    pass

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

    # Deal cards to each player one at a time until each player has the required number of cards:
    for i in range(1, 1 + no_cards_per_player):

        # Pick a random card:
        one_card = random.choice(deck_of_cards)

        # Give the random card to the player:
        player_1_hand.append (one_card)
        deck_of_cards.remove (one_card)

        # Pick another random card:
        one_card = random.choice(deck_of_cards)

        # Give the random card to the computer player:
        computer_hand.append (one_card)
        deck_of_cards.remove (one_card)

###########################################################################################

def kick_trump_card():

    # Pick a random card:
    one_card = random.choice(deck_of_cards)

    # Make  the random card the trump card and remove it from the deck:
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

def put_cards_in_frames():

    # Place the trump card in its frame:
    trump_label.configure(text = trump_card[0])

    # Place the dealer cards in their frames:
    dealer_frame_card_1_label.configure(text = computer_hand[0])
    dealer_frame_card_2_label.configure(text = computer_hand[1])
    dealer_frame_card_3_label.configure(text = computer_hand[2])

    # Place the player cards in their frames:
    player_frame_card_1_label.configure(text = player_1_hand[0])
    player_frame_card_2_label.configure(text = player_1_hand[1])
    player_frame_card_3_label.configure(text = player_1_hand[2])

###########################################################################################
# Main program:
###########################################################################################

# Create the application:
create_application()

# Create frames to hold the cards:
create_frames()

# Create buttons for the game:
#create_buttons(root)

# Create a new deck of cards:
create_new_deck()

# Deal the cards to all players:
deal_cards()

# Kick the trump card:
kick_trump_card()

# Place cards in the frames:
put_cards_in_frames()


root.mainloop()