###########################################################################################

# Import libraries:
from tkinter import *
from PIL import Image, ImageTk
import random

###########################################################################################

# Declare global variables:
deck_of_cards = []
no_cards_per_player = 6

# These set the size of the frames which holds the cards:
global frame_width
frame_width = 30

global frame_height
frame_height = 180

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
    root.configure(background="green")

    # Enable fullscreen mode:
    #   root.attributes('-fullscreen', True)
    # Bind the Escape key to exit fullscreen mode:
    #   root.bind('<Escape>', exit_fullscreen)
    root.geometry("1400x800")

###########################################################################################

def exit_fullscreen(event=None):

    # This functions changes game to full screen:
    root.attributes('-fullscreen', False)

###########################################################################################

def create_frames():

    ###########################################################################################
    # Split main application window into (1) side-bar to display points and (2) main board where cards are played:
    ###########################################################################################
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=2)    
    root.columnconfigure(1, weight=3)    
    root.columnconfigure(2, weight=2)

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
    trump_frame.grid(row=0, column=1, padx=20, ipadx=40, pady=20)

    global trump_label
    trump_label = Label(trump_frame, text='1. This is a Label.')
    trump_label.place(x=0, y=5)

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

    global dealer_frame_card_2
    dealer_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    dealer_frame_card_2.grid(row=1, column=1, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_2_label
    dealer_frame_card_2_label = Label(dealer_frame_card_2, text='1. This is a Label.')
    dealer_frame_card_2_label.place(x=0, y=5)

    global dealer_frame_card_3
    dealer_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_3.grid(row=1, column=2, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_3_label
    dealer_frame_card_3_label = Label(dealer_frame_card_3, text='1. This is a Label.')
    dealer_frame_card_3_label.place(x=0, y=5)

    global dealer_frame_card_4
    dealer_frame_card_4 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_4.grid(row=1, column=3, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_4_label
    dealer_frame_card_4_label = Label(dealer_frame_card_4, text='1. This is a Label.')
    dealer_frame_card_4_label.place(x=0, y=5)

    global dealer_frame_card_5
    dealer_frame_card_5 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_5.grid(row=1, column=4, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_5_label
    dealer_frame_card_5_label = Label(dealer_frame_card_5, text='1. This is a Label.')
    dealer_frame_card_5_label.place(x=0, y=5)

    global dealer_frame_card_6
    dealer_frame_card_6 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="", bd=0, background="#3ce663")
    dealer_frame_card_6.grid(row=1, column=5, padx=20, ipadx=40, pady=20)

    global dealer_frame_card_6_label
    dealer_frame_card_6_label = Label(dealer_frame_card_6, text='1. This is a Label.')
    dealer_frame_card_6_label.place(x=0, y=5)

    ##########################################################################################################################
    # Create frames to show cards that are played within each round:
    ##########################################################################################################################
    
    # Add text indicating this section contains the dealer hand:
    player_frame_card_label = Label(frame_main_board, text="Playing area", background="black", foreground="white", font=("Arial", 12, "bold"), width=100)
    player_frame_card_label.grid(row=3, column=0, columnspan=6, padx=5, pady=5)
    
    global round_frame_card_1
    round_frame_card_1 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, bd=0)    
    round_frame_card_1.grid(row=4, column=2, padx=20, ipadx=40, pady=20)

    global round_frame_card_1_label   
    round_frame_card_1_label = Label(round_frame_card_1)
    round_frame_card_1_label.place(x=0, y=5)
    my_image = resize_card_image("blank_card")
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image 

    # reate frame to hold card 2 for each round:
    global round_frame_card_2
    round_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, bd=0)    
    round_frame_card_2.grid(row=4, column=3, padx=20, ipadx=40, pady=20)

    global round_frame_card_2_label
    round_frame_card_2_label = Label(round_frame_card_2, text='')
    round_frame_card_2_label.place(x=0, y=5)   
    my_image = resize_card_image("blank_card")
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

    global player_frame_card_2
    player_frame_card_2 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_2.grid(row=6, column=1, padx=20, ipadx=40, pady=20)
    player_frame_card_2.bind("<Button-1>", player_frame_card_2_click)

    global player_frame_card_2_label
    player_frame_card_2_label = Label(player_frame_card_2, text='1. This is a Label.')
    player_frame_card_2_label.place(x=0, y=5)

    global player_frame_card_3
    player_frame_card_3 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_3.grid(row=6, column=2, padx=20, ipadx=40, pady=20)
    player_frame_card_3.bind("<Button-1>", player_frame_card_3_click)

    global player_frame_card_3_label
    player_frame_card_3_label = Label(player_frame_card_3, text='1. This is a Label.')
    player_frame_card_3_label.place(x=0, y=5)

    global player_frame_card_4
    player_frame_card_4 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_4.grid(row=6, column=3, padx=20, ipadx=40, pady=20)
    player_frame_card_4.bind("<Button-1>", player_frame_card_4_click)

    global player_frame_card_4_label
    player_frame_card_4_label = Label(player_frame_card_4, text='1. This is a Label.')
    player_frame_card_4_label.place(x=0, y=5)

    global player_frame_card_5
    player_frame_card_5 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_5.grid(row=6, column=4, padx=20, ipadx=40, pady=20)
    player_frame_card_5.bind("<Button-1>", player_frame_card_5_click)

    global player_frame_card_5_label
    player_frame_card_5_label = Label(player_frame_card_5, text='1. This is a Label.')
    player_frame_card_5_label.place(x=0, y=5)

    global player_frame_card_6
    player_frame_card_6 = LabelFrame(frame_main_board, width = frame_width, height = frame_height, text="",bd=0, background="#3ce663")
    player_frame_card_6.grid(row=6, column=5, padx=20, ipadx=40, pady=20)
    player_frame_card_6.bind("<Button-1>", player_frame_card_6_click)

    global player_frame_card_6_label
    player_frame_card_6_label = Label(player_frame_card_6, text='1. This is a Label.')
    player_frame_card_6_label.place(x=0, y=5)

###########################################################################################

def player_frame_card_1_click (event):

    print("Frame 1 was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[0])
    round_frame_card_1_label.configure(image=my_image)
    round_frame_card_1_label.image = my_image 

    # Now hide the card from the player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_1_label.configure(image=my_image)
    player_frame_card_1_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[0])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

     # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_1_label.configure(image=my_image)
    dealer_frame_card_1_label.image = my_image 

    #dermine_round_winner()

###########################################################################################

def player_frame_card_2_click (event):

    print("Frame 2 was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[1])
    round_frame_card_1_label.configure(image=my_image) 
    round_frame_card_1_label.image = my_image

    # Now hide the card from the player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_2_label.configure(image=my_image)
    player_frame_card_2_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[1])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_2_label.configure(image=my_image)
    dealer_frame_card_2_label.image = my_image 

    determine_round_winner()

###########################################################################################

def player_frame_card_3_click (event):

    print("Frame 3 was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[2])
    round_frame_card_1_label.configure(image=my_image) 
    round_frame_card_1_label.image = my_image

    # Now hide the card from the player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_3_label.configure(image=my_image)
    player_frame_card_3_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[2])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_3_label.configure(image=my_image)
    dealer_frame_card_3_label.image = my_image 

    determine_round_winner()

def player_frame_card_4_click (event):

    print("Frame was 4 clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[3])
    round_frame_card_1_label.configure(image=my_image) 
    round_frame_card_1_label.image = my_image

    # Now hide the card from the player's hand:
    #player_frame_card_4.grid_remove()
    my_image = resize_card_image("blank_card")
    player_frame_card_4_label.configure(image=my_image)
    player_frame_card_4_label.image = my_image     

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[3])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_4_label.configure(image=my_image)
    dealer_frame_card_4_label.image = my_image 

    determine_round_winner()    

def player_frame_card_5_click (event):

    print("Frame was 5 clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[4])
    round_frame_card_1_label.configure(image=my_image) 
    round_frame_card_1_label.image = my_image

    # Now hide the card from the player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_5_label.configure(image=my_image)
    player_frame_card_5_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[4])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_5_label.configure(image=my_image)
    dealer_frame_card_5_label.image = my_image 

    determine_round_winner()    

def player_frame_card_6_click (event):

    print("Frame 6 was clicked")

    # Player clicked the card to play, so move the card from the player frame to the round frame:
    my_image = resize_card_image(player_1_hand[5])
    round_frame_card_1_label.configure(image=my_image) 
    round_frame_card_1_label.image = my_image

    # Now hide the card from the player's hand:
    my_image = resize_card_image("blank_card")
    player_frame_card_6_label.configure(image=my_image)
    player_frame_card_6_label.image = my_image 

    # Now is the computer's turn to play a card, so move the card from the computer frame to the round frame:
    my_image = resize_card_image(computer_hand[5])
    round_frame_card_2_label.configure(image=my_image)
    round_frame_card_2_label.image = my_image

    # Now hide the card from the computer's hand:
    my_image = resize_card_image("blank_card")
    dealer_frame_card_6_label.configure(image=my_image)
    dealer_frame_card_6_label.image = my_image 

    determine_round_winner()        

###########################################################################################

def determine_round_winner():
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
                tempcard = (f"Jack_of_{one_suit}")
            elif one_card == 12:
                tempcard = (f"Queen_of_{one_suit}")
            elif one_card == 13:
                tempcard = (f"King_of_{one_suit}")
            elif one_card == 14:
                tempcard = (f"Ace_of_{one_suit}")
            else:
                tempcard = (f"{one_card}_of_{one_suit}")
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
    my_image = resize_card_image(trump_card[0])
    trump_label.configure(image=my_image)
    trump_label.image = my_image 

    # Place the dealer cards in their frames:
    my_image = resize_card_image(computer_hand[0])
    dealer_frame_card_1_label.configure(image=my_image)
    dealer_frame_card_1_label.image = my_image 

    my_image = resize_card_image(computer_hand[1])
    dealer_frame_card_2_label.configure(image=my_image)
    dealer_frame_card_2_label.image = my_image 

    my_image = resize_card_image(computer_hand[2])
    dealer_frame_card_3_label.configure(image=my_image)
    dealer_frame_card_3_label.image = my_image 

    my_image = resize_card_image(computer_hand[3])
    dealer_frame_card_4_label.configure(image=my_image)
    dealer_frame_card_4_label.image = my_image 

    my_image = resize_card_image(computer_hand[4])
    dealer_frame_card_5_label.configure(image=my_image)
    dealer_frame_card_5_label.image = my_image 

    my_image = resize_card_image(computer_hand[5])
    dealer_frame_card_6_label.configure(image=my_image)
    dealer_frame_card_6_label.image = my_image             

    # Place the player cards in their frames:
    my_image = resize_card_image(player_1_hand[0])
    player_frame_card_1_label.configure(image=my_image)
    player_frame_card_1_label.image = my_image 
    player_frame_card_1_label.bind("<Button-1>", player_frame_card_1_click)

    my_image = resize_card_image(player_1_hand[1])
    player_frame_card_2_label.configure(image=my_image)
    player_frame_card_2_label.image = my_image 
    player_frame_card_2_label.bind("<Button-1>", player_frame_card_2_click)

    my_image = resize_card_image(player_1_hand[2])
    player_frame_card_3_label.configure(image=my_image)
    player_frame_card_3_label.image = my_image 
    player_frame_card_3_label.bind("<Button-1>", player_frame_card_3_click)

    my_image = resize_card_image(player_1_hand[3])
    player_frame_card_4_label.configure(image=my_image)
    player_frame_card_4_label.image = my_image 
    player_frame_card_4_label.bind("<Button-1>", player_frame_card_4_click)

    my_image = resize_card_image(player_1_hand[4])
    player_frame_card_5_label.configure(image=my_image)
    player_frame_card_5_label.image = my_image 
    player_frame_card_5_label.bind("<Button-1>", player_frame_card_5_click)

    my_image = resize_card_image(player_1_hand[5])
    player_frame_card_6_label.configure(image=my_image)
    player_frame_card_6_label.image = my_image 
    player_frame_card_6_label.bind("<Button-1>", player_frame_card_6_click)    

    # Indicate to user they can start playing:
    player_frame_card_label = Label(frame_main_board, text="Your hand", background="red", foreground="white", font=("Arial", 12, "bold"), width=100)
    player_frame_card_label.grid(row=5, column=0, columnspan=6, padx=5, pady=5)
    player_frame_card_label.config(text='Your hand - Your play')
    

###########################################################################################

def resize_card_image(card):

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