# Import libraries:
from tkinter import *

def shuffle_deck():
    
    # Create a deck of cards:
    suits = ["hearts","diamonds","clubs","spades"]
    cards = [x for x in range (2,14)]

    for one_suit in suits:
        for one_card in cards:
            print (f"{one_card} of {one_suit}")


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

# Put cards in dealer frame:
dealer_label = Label(dealer_frame, text ="Test1")
dealer_label.pack(pady=50)

# Put cards in player frame:
player_label = Label(player_frame, text = "Test2")
player_label.pack(pady=50)

# Create button to shuffe the deck:
shuffle_button = Button(root, text="Shuffle the Deck")
shuffle_button.pack(pady=20)

# Create button to deal the cards:
deal_button = Button(root, text="Deal the Cards")
deal_button.pack(pady=20)


root.mainloop()

print ("Completed my run 2342342234")
