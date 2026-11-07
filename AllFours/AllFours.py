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

def create_frames():

    # Split main application window into (1) side-bar to display points and (2) main board where cards are played
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)    
    root.columnconfigure(1, weight=5)

    # Create frame for side-bar:
    global frame_left_sidebar
    frame_left_sidebar = Frame(root, bg="yellow")
    frame_left_sidebar.grid(row = 0, column=0, sticky="nsew")

    # Create frame where cards are played
    global frame_main_board
    frame_main_board = Frame(root, bg="#3ce663", bd=2)
    frame_main_board.grid(row = 0, column=1, sticky="nsew")


###########################################################################################
# Main program:
###########################################################################################

# Create the application:
create_application()

# Create frames to hold the cards:
create_frames()

root.mainloop()