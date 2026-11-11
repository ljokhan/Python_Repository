###########################################################################################

# Import libraries:
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import time

###########################################################################################

# Declare global variables:
deck_of_cards = []
no_cards_per_player = 6
num_chalks_dealer = 0
num_chalks_player = 0

# These store the total point for a single round of play:
global points_this_round_player
points_this_round_player = 0

global points_this_round_dealer
points_this_round_dealer = 0

# These set the size of the frames which holds the cards:
global frame_width
frame_width = 30

global frame_height
frame_height = 180

# These global variables hold the cards for each player and the trump card:
all_playing_cards = []
player_1_hand = []
computer_hand = []
board_hand = ["placeholder1", "placeholder2"]
trump_card = []

###########################################################################################

def create_application ():

    # Create the main application window:
    global root
    root = Tk()
    root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")
    root.configure(background="green")

    # Enable fullscreen mode:
    #   root.attributes('-fullscreen', True)
    # Bind the Escape key to exit fullscreen mode:
    #   root.bind('<Escape>', exit_fullscreen)
    root.geometry("1400x800")

###########################################################################################

def exit_fullscreen (event=None):

    # This functions changes game to full screen:
    root.attributes('-fullscreen', False)

###########################################################################################

def create_frames ():

    ###########################################################################################
    # Split main application window into (1) side-bar to display points and (2) main board where cards are played:
    ###########################################################################################
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=2)    
    root.columnconfigure(1, weight=3)    
    root.columnconfigure(2, weight=2)
    
    # Prepage image of the back of a playing card, so we can start the game with all cards turned over:
    my_image = resize_card_image("back_of_playing_card")

    ###########################################################################################
    # Create frame for left side-bar:
    ###########################################################################################
    global frame_left_sidebar
    frame_left_sidebar = Frame(root, bg="yellow")
    frame_left_sidebar.grid(row = 0, column=0, sticky="nsew")

    ###########################################################################################
    # Create frame where cards are played:
    ###########################################################################################
    global frame_main_board
    frame_main_board = Frame(root, bg="#3ce663", bd=2)
    frame_main_board.grid(row = 0, column=1, sticky="nsew")

    ###########################################################################################
    # Create frame for rightside-bar:
    ###########################################################################################
    global frame_right_sidebar
    frame_right_sidebar = Frame(root, bg="yellow")
    frame_right_sidebar.grid(row = 0, column=2, sticky="nsew")

    ###########################################################################################
    # Create frame for trump card:
    ###########################################################################################

    global trump_frame
    trump_frame = LabelFrame(frame_right_sidebar, width = frame_width, height = frame_height, bd=0, text="Trump", background="yellow", font=("Arial", 12))
    trump_frame.grid(row=0, column=0, padx=20, ipadx=40, pady=20)

    global trump_label
    trump_label = Label(trump_frame, text='1. This is a Label.')
    trump_label.place(x=0, y=5)

    # Add image of overturned card:
    trump_label.configure(image=my_image)
    trump_label.image = my_image 

    ###########################################################################################
    # Create frames which show dealer cards:
    ###########################################################################################
    
    # Add text indicating this section contains the dealer hand:
    frame_main_board_label = Label(frame_main_board, text="Dealer hand", background="black", foreground="white", font=("Arial", 12, "bold"), width=100)
    frame_main_board_label.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        
    global dealer_frame_card_1
    dealer_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    dealer_frame_card_1.grid(row=1, column=0, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_1_label
    dealer_frame_card_1_label = Label(dealer_frame_card_1, text='1. This is a Label.')
    dealer_frame_card_1_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_1_label.configure(image=my_image)
    dealer_frame_card_1_label.image = my_image           

    global dealer_frame_card_2
    dealer_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    dealer_frame_card_2.grid(row=1, column=1, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_2_label
    dealer_frame_card_2_label = Label(dealer_frame_card_2, text='1. This is a Label.')
    dealer_frame_card_2_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_2_label.configure(image=my_image)
    dealer_frame_card_2_label.image = my_image         

    global dealer_frame_card_3
    dealer_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_3.grid(row=1, column=2, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_3_label
    dealer_frame_card_3_label = Label(dealer_frame_card_3, text='1. This is a Label.')
    dealer_frame_card_3_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_3_label.configure(image=my_image)
    dealer_frame_card_3_label.image = my_image       

    global dealer_frame_card_4
    dealer_frame_card_4 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_4.grid(row=1, column=3, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_4_label
    dealer_frame_card_4_label = Label(dealer_frame_card_4, text='1. This is a Label.')
    dealer_frame_card_4_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_4_label.configure(image=my_image)
    dealer_frame_card_4_label.image = my_image         

    global dealer_frame_card_5
    dealer_frame_card_5 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_5.grid(row=1, column=4, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_5_label
    dealer_frame_card_5_label = Label(dealer_frame_card_5, text='1. This is a Label.')
    dealer_frame_card_5_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_5_label.configure(image=my_image)
    dealer_frame_card_5_label.image = my_image     

    global dealer_frame_card_6
    dealer_frame_card_6 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_6.grid(row=1, column=5, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_6_label
    dealer_frame_card_6_label = Label(dealer_frame_card_6, text='1. This is a Label.')
    dealer_frame_card_6_label.place(x=0, y=5)

    # Add image of overturned card:
    dealer_frame_card_6_label.configure(image=my_image)
    dealer_frame_card_6_label.image = my_image 

    ##########################################################################################################################
    # Create frames to show cards that are played within each round:
    ##########################################################################################################################
    
    # Resize the image of the back of a playing card, so we can start the game with all card turned over:
    #my_image = resize_card_image("back_of_playing_card")

    # Add text indicating this section contains the dealer hand:
    player_frame_card_label = Label(frame_main_board, text="Playing area", background="black", foreground="white", font=("Arial", 12, "bold"), width=100)
    player_frame_card_label.grid(row=3, column=0, columnspan=6, padx=5, pady=5)
    
    global round_frame_card_1
    round_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, bd=0, background="#3ce663")    
    round_frame_card_1.grid(row=4, column=2, padx=20, ipadx=40, pady=20)

    global round_frame_card_1_label   
    round_frame_card_1_label = Label(round_frame_card_1)
    round_frame_card_1_label.place(x=0, y=5)
    #my_image = resize_card_image("blank_card")
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image 

    # reate frame to hold card 2 for each round:
    global round_frame_card_2
    round_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, bd=0, background="#3ce663")    
    round_frame_card_2.grid(row=4, column=3, padx=20, ipadx=40, pady=20)

    global round_frame_card_2_label
    round_frame_card_2_label = Label(round_frame_card_2)
    round_frame_card_2_label.place(x=0, y=5)   
    #my_image = resize_card_image("blank_card")
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image 

    ##########################################################################################################################
    # Create clickable frames to show player cards:
    ##########################################################################################################################

    # Add text indicating this section contains the dealer hand:
    player_frame_card_label = Label(frame_main_board, text="Your hand", background="black", foreground="white", font=("Arial", 12, "bold"), width=100)
    player_frame_card_label.grid(row=5, column=0, columnspan=6, padx=5, pady=5)


   
    global player_frame_card_1
    player_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_1.grid(row=6, column=0, padx=20, ipadx=40, pady=20)
    player_frame_card_1.bind("<Button-1>", player_frame_card_1_click)

    global player_frame_card_1_label
    player_frame_card_1_label = Label(player_frame_card_1, text='1. This is a Label.')
    player_frame_card_1_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_1_label.configure(image=my_image)
    player_frame_card_1_label.image = my_image 

    global player_frame_card_2
    player_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_2.grid(row=6, column=1, padx=20, ipadx=40, pady=20)
    player_frame_card_2.bind("<Button-1>", player_frame_card_2_click)

    global player_frame_card_2_label
    player_frame_card_2_label = Label(player_frame_card_2, text='1. This is a Label.')
    player_frame_card_2_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_2_label.configure(image=my_image)
    player_frame_card_2_label.image = my_image 

    global player_frame_card_3
    player_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_3.grid(row=6, column=2, padx=20, ipadx=40, pady=20)
    player_frame_card_3.bind("<Button-1>", player_frame_card_3_click)

    global player_frame_card_3_label
    player_frame_card_3_label = Label(player_frame_card_3, text='1. This is a Label.')
    player_frame_card_3_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_3_label.configure(image=my_image)
    player_frame_card_3_label.image = my_image 

    global player_frame_card_4
    player_frame_card_4 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_4.grid(row=6, column=3, padx=20, ipadx=40, pady=20)
    player_frame_card_4.bind("<Button-1>", player_frame_card_4_click)

    global player_frame_card_4_label
    player_frame_card_4_label = Label(player_frame_card_4, text='1. This is a Label.')
    player_frame_card_4_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_4_label.configure(image=my_image)
    player_frame_card_4_label.image = my_image 

    global player_frame_card_5
    player_frame_card_5 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_5.grid(row=6, column=4, padx=20, ipadx=40, pady=20)
    player_frame_card_5.bind("<Button-1>", player_frame_card_5_click)

    global player_frame_card_5_label
    player_frame_card_5_label = Label(player_frame_card_5, text='1. This is a Label.')
    player_frame_card_5_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_5_label.configure(image=my_image)
    player_frame_card_5_label.image = my_image     

    global player_frame_card_6
    player_frame_card_6 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_6.grid(row=6, column=5, padx=20, ipadx=40, pady=20)
    player_frame_card_6.bind("<Button-1>", player_frame_card_6_click)

    global player_frame_card_6_label
    player_frame_card_6_label = Label(player_frame_card_6, text='1. This is a Label.')
    player_frame_card_6_label.place(x=0, y=5)

    # Add image of overturned card:
    player_frame_card_6_label.configure(image=my_image)
    player_frame_card_6_label.image = my_image   

###########################################################################################

def player_frame_card_1_click (event):

    print("Frame 1 was clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[0]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image 
    
    # Replace the player card with NULL:
    player_1_hand[0] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_1_label.configure(image=my_image)
    player_frame_card_1_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[0]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[0] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_1_label.configure(image=my_image)
    dealer_frame_card_1_label.image = my_image 

    determine_winner_of_this_hand()

###########################################################################################

def player_frame_card_2_click (event):

    print("Frame 2 was clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[1]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image
    
    # Replace the player card with NULL:
    player_1_hand[1] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_2_label.configure(image=my_image)
    player_frame_card_2_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[1]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[1] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_2_label.configure(image=my_image)
    dealer_frame_card_2_label.image = my_image 
    
    determine_winner_of_this_hand()

###########################################################################################

def player_frame_card_3_click (event):

    print("Frame 3 was clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[2]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image
    
    # Replace the player card with NULL:
    player_1_hand[2] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_3_label.configure(image=my_image)
    player_frame_card_3_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[2]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[1] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_3_label.configure(image=my_image)
    dealer_frame_card_3_label.image = my_image 

    determine_winner_of_this_hand()

###########################################################################################

def player_frame_card_4_click (event):
    
###########################################################################################

    print("Frame was 4 clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[3]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image
    
    # Replace the player card with NULL:
    player_1_hand[3] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_4_label.configure(image=my_image)
    player_frame_card_4_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[3]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[3] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_4_label.configure(image=my_image)
    dealer_frame_card_4_label.image = my_image 

    determine_winner_of_this_hand()    

###########################################################################################

def player_frame_card_5_click (event):

    print("Frame was 5 clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[4]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image
    
    # Replace the player card with NULL:
    player_1_hand[4] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_5_label.configure(image=my_image)
    player_frame_card_5_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[4]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[4] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_5_label.configure(image=my_image)
    dealer_frame_card_5_label.image = my_image 

    determine_winner_of_this_hand()    

###########################################################################################

def player_frame_card_6_click (event):

    print("Frame 6 was clicked")

    # Player clicked the card to play, so move the card from the player hand to the board:
    board_hand[0] = player_1_hand[5]

    # Generate image to place on the board:
    my_image = resize_card_image(board_hand[0].card_name)
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image
    
    # Replace the player card with NULL:
    player_1_hand[5] = None

    # Generate image of a blank card and place it in player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_6_label.configure(image=my_image)
    player_frame_card_6_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the board:
    board_hand[1] = computer_hand[5]
    
    # Generate image to place on the board:
    my_image = resize_card_image (board_hand[1].card_name)
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Replace the dealer card with NULL:
    computer_hand[5] = None

    # Generate image of a blank card and place it in dealer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_6_label.configure(image=my_image)
    dealer_frame_card_6_label.image = my_image 
    
    determine_winner_of_this_hand()        

###########################################################################################

def calculate_points_per_card (one_card):

    #points_per_card = 0

    if one_card.card_value < 10:

        # No points for cards 2 -> 9:
        points_per_card = 0

    elif one_card.card_value == 10:

        # 10-card gets 10 points:
        points_per_card = 10
    
    elif one_card.card_value == 11:

        # Jack gets 1 point:
        points_per_card = 1

    elif one_card.card_value == 12:

        # Queen  gets 2 points:
        points_per_card = 2

    elif one_card.card_value == 13:

        # King gets 3 points:
        points_per_card = 3
    
    elif one_card.card_value == 14:

        # Ace gets 3 points:
        points_per_card = 4

    return points_per_card

###########################################################################################

def calculate_points_per_hand ():

    points_per_hand = 0

    points_per_hand = points_per_hand + calculate_points_per_card(board_hand[0])

    points_per_hand = points_per_hand + calculate_points_per_card(board_hand[1])

    return points_per_hand

###########################################################################################

def determine_winner_of_this_hand ():

    global points_this_round_player
    global points_this_round_dealer

    winner = "* ERROR - NO WINNER CALCULATED*"

    # Determine if player or dealer wins this round:
    if (board_hand[0].card_suit == trump_card[0].card_suit) and (board_hand[1].card_suit != trump_card[0].card_suit):

        # Player has trump card. Dealer does not have trump. Player wins:
        winner = 'player'

    elif (board_hand[0].card_suit != trump_card[0].card_suit) and (board_hand[1].card_suit == trump_card[0].card_suit):

        # Dealer has trump card. Player does not have trump. Dealer wins:
        winner = 'dealer'
    
    elif (board_hand[0].card_suit == trump_card[0].card_suit) and (board_hand[1].card_suit == trump_card[0].card_suit) and \
            (board_hand[0].card_value > board_hand[1].card_value)   :

        # Both have trump cards. Player  card is higher. Player wins:
        winner = 'player'

    elif (board_hand[0].card_suit == trump_card[0].card_suit) and (board_hand[1].card_suit == trump_card[0].card_suit) and \
            (board_hand[0].card_value < board_hand[1].card_value)   :

        # Both have trump cards. Dealer card is higher. Dealer wins:
        winner = 'dealer'

    elif (board_hand[0].card_suit != trump_card[0].card_suit) and (board_hand[1].card_suit != trump_card[0].card_suit) and \
            (board_hand[0].card_suit == board_hand[1].card_suit) and (board_hand[0].card_value > board_hand[1].card_value)  :

        # Neither have trump cards. Both have same suit. Player card is higher. Player wins:
        winner = 'player'        

    elif (board_hand[0].card_suit != trump_card[0].card_suit) and (board_hand[1].card_suit != trump_card[0].card_suit) and \
            (board_hand[0].card_suit == board_hand[1].card_suit) and (board_hand[0].card_value < board_hand[1].card_value)  :

        # Neither have trump cards. Both have same suit. Dealer card is higher. Dealer wins:
        winner = 'dealer'  

    elif (board_hand[0].card_suit != trump_card[0].card_suit) and (board_hand[1].card_suit != trump_card[0].card_suit) and \
            (board_hand[0].card_suit != board_hand[1].card_suit) :

        # Neither have trump cards. Both have different suits. Player played 1st, so his card makes him the winner:
        winner = 'player'  

    # Calculate points for this hand:
    points_this_hand = calculate_points_per_hand()
    #messagebox.showinfo("Points this hand", points_this_hand)

    # Add points for this hand to the total point counter for this round of play:
    if winner == 'player':
        points_this_round_player += points_this_hand
    elif winner == 'dealer':
        points_this_round_dealer += points_this_hand

    # Display message showing who won and how many points were won this hand:
    if points_this_hand == 0:
        winner_of_current_hand_label.configure(text=winner.title() + " wins!")
    elif points_this_hand == 1:
        winner_of_current_hand_label.configure(text=winner.title() + " wins " + points_this_hand.__str__() + " point!")
    elif points_this_hand > 1:
            winner_of_current_hand_label.configure(text=winner.title() + " wins " + points_this_hand.__str__() + " points!")

    # Update labels so player can see total points this round:
    points_dealer_label.configure (text="Dealer points: " + points_this_round_dealer.__str__())
    points_player_label.configure (text="Player points: " + points_this_round_player.__str__())

###########################################################################################

###########################################################################################

def create_new_deck ():

    # Create class to store each playing card:
    class class_playing_card:
        def __init__(self, card_name, card_value, card_suit, card_image_path, board_location):
            self.card_name = card_name
            self.card_value = card_value
            self.card_suit = card_suit
            self.card_image_path = card_image_path
            self.board_location = board_location
    
    # Create suits and individual cards:
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    card_values = [x for x in range (2,14)]

    # Create a full deck of cards:
    for one_suit in suits:
        for one_card_value in card_values:
            if one_card_value == 11:
                tempcard = (f"Jack_of_{one_suit}")
            elif one_card_value == 12:
                tempcard = (f"Queen_of_{one_suit}")
            elif one_card_value == 13:
                tempcard = (f"King_of_{one_suit}")
            elif one_card_value == 14:
                tempcard = (f"Ace_of_{one_suit}")
            else:
                tempcard = (f"{one_card_value}_of_{one_suit}")
            deck_of_cards.append(tempcard)

            # Generate one instance of the playing card class:
            one_card = class_playing_card (tempcard, one_card_value, one_suit, "./AllFours/PlayingCardImages/" + tempcard + ".png", None)

            # Append playing card to list:
            all_playing_cards.append(one_card)

    for one_playing_card in all_playing_cards:
        print (one_playing_card.card_value)

###########################################################################################

def deal_cards ():

    # Deal cards to each player one at a time until each player has the required number of cards:
    for i in range(1, 1 + no_cards_per_player):

        # Pick a random card:
        #one_card = random.choice(deck_of_cards)
        one_card = random.choice(all_playing_cards)

        # Add random card to the player hand:
        player_1_hand.append (one_card)
        all_playing_cards.remove (one_card)

        # Pick another random card:
        one_card = random.choice(all_playing_cards)

        # Add random card to the computer hand:
        computer_hand.append (one_card)
        all_playing_cards.remove (one_card)

###########################################################################################

def kick_trump_card ():

    # Pick a random card:
    one_card = random.choice(all_playing_cards)

    # Add random card the trump list and remove it from the deck:
    trump_card.append (one_card)
    all_playing_cards.remove (one_card)

###########################################################################################

def create_buttons ():

    # Create button to shuffle the deck:
    shuffle_button = Button(frame_right_sidebar, text="Shuffle and Deal", command=begin_game)
    shuffle_button.grid(row=1, column=0, padx=5, pady=5)

###########################################################################################

def create_point_counters ():

    # This label shows the winner for this hand:
    global winner_of_current_hand_label
    winner_of_current_hand_label = Label(frame_right_sidebar, text="Current hand results", background="black", foreground="white", font=("Arial", 12, "bold"), width=20)
    winner_of_current_hand_label.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # This label shows the total points for the dealer:
    global points_dealer_label
    points_dealer_label = Label(frame_right_sidebar, text="Dealer points: 0", background="black", foreground="white", font=("Arial", 12, "bold"), width=20)
    points_dealer_label.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    # This label shows the total points for the player:
    global points_player_label
    points_player_label = Label(frame_right_sidebar, text="Player points: 0", background="black", foreground="white", font=("Arial", 12, "bold"), width=20)
    points_player_label.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

###########################################################################################

def begin_game ():
  
    # Deal the cards to all players:
    deal_cards()

    # Kick the trump card:
    kick_trump_card()

    # Place cards in the frames:
    put_cards_in_frames()

###########################################################################################

def put_cards_in_frames ():

    #######################################################################################
    # Trump card section:
    #######################################################################################
    
    # Place the trump card in its frame:
    my_image = resize_card_image(trump_card[0].card_name)
    trump_label.configure(image=my_image)
    trump_label.image = my_image 

    #######################################################################################
    # Dealer card section
    #######################################################################################
    my_image = resize_card_image(computer_hand[0].card_name)
    dealer_frame_card_1_label.configure(image=my_image)
    dealer_frame_card_1_label.image = my_image 

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D1'

    my_image = resize_card_image(computer_hand[1].card_name)
    dealer_frame_card_2_label.configure(image=my_image)
    dealer_frame_card_2_label.image = my_image  

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D2'

    my_image = resize_card_image(computer_hand[2].card_name)
    dealer_frame_card_3_label.configure(image=my_image)
    dealer_frame_card_3_label.image = my_image 

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D3'

    my_image = resize_card_image(computer_hand[3].card_name)
    dealer_frame_card_4_label.configure(image=my_image)
    dealer_frame_card_4_label.image = my_image 

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D4'

    my_image = resize_card_image(computer_hand[4].card_name)
    dealer_frame_card_5_label.configure(image=my_image)
    dealer_frame_card_5_label.image = my_image 

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D5'    

    my_image = resize_card_image(computer_hand[5].card_name)
    dealer_frame_card_6_label.configure(image=my_image)
    dealer_frame_card_6_label.image = my_image      

    # Update location so we know which card is in which position on the screen:
    computer_hand[0].card_location = 'D6'           

    #######################################################################################
    # Player card section
    #######################################################################################

    # Place the player cards in their frames:
    my_image = resize_card_image(player_1_hand[0].card_name)
    player_frame_card_1_label.configure(image=my_image)
    player_frame_card_1_label.image = my_image 
    player_frame_card_1_label.bind("<Button-1>", player_frame_card_1_click)

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P1'

    my_image = resize_card_image(player_1_hand[1].card_name)
    player_frame_card_2_label.configure(image=my_image)
    player_frame_card_2_label.image = my_image 
    player_frame_card_2_label.bind("<Button-1>", player_frame_card_2_click)

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P2'    

    my_image = resize_card_image(player_1_hand[2].card_name)
    player_frame_card_3_label.configure(image=my_image)
    player_frame_card_3_label.image = my_image 
    player_frame_card_3_label.bind("<Button-1>", player_frame_card_3_click)

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P3'    

    my_image = resize_card_image(player_1_hand[3].card_name)
    player_frame_card_4_label.configure(image=my_image)
    player_frame_card_4_label.image = my_image 
    player_frame_card_4_label.bind("<Button-1>", player_frame_card_4_click)

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P4'    

    my_image = resize_card_image(player_1_hand[4].card_name)
    player_frame_card_5_label.configure(image=my_image)
    player_frame_card_5_label.image = my_image 
    player_frame_card_5_label.bind("<Button-1>", player_frame_card_5_click)

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P5'    

    my_image = resize_card_image(player_1_hand[5].card_name)
    player_frame_card_6_label.configure(image=my_image)
    player_frame_card_6_label.image = my_image 
    player_frame_card_6_label.bind("<Button-1>", player_frame_card_6_click)   

    # Update location so we know which card is in which position on the screen:
    player_1_hand[0].card_location = 'P6'     

    # Indicate to user they can start playing:
    player_frame_card_label = Label(frame_main_board, text="Your hand", background="red", foreground="white", font=("Arial", 12, "bold"), width=100)
    player_frame_card_label.grid(row=5, column=0, columnspan=6, padx=5, pady=5)
    
###########################################################################################

def resize_card_image (card):

    image_path = "./AllFours/PlayingCardImages/" + card + ".png"
    pil_image = Image.open(image_path)
    resized_image = pil_image.resize((100, 150), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)

    return tk_image 

###########################################################################################

def exit_game():

    # This will close the game window:
    root.destroy() 
    
###########################################################################################
# Main program:
###########################################################################################

# Create the All Fours game application:
create_application()

# Create frames to hold the cards:
create_frames()

# Create a new deck of cards:
create_new_deck()

# Create buttons to play the game:
create_buttons()

# Create counter for points:
create_point_counters ()

root.mainloop()

