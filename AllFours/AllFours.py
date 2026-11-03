# Import libraries:
from tkinter import *

# Configure the outer screen:
root = Tk()
root.title("All-Fo's -- The most popular card game of Trinidad & Tobago")
root.geometry("900x500")
root.configure(background="green")

# Create outer frame for the game:
my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

# Create frame for dealer cards:
dealer_frame = LabelFrame(my_frame, text="Dealer",bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

# Create frame for player cards:
player_frame = LabelFrame(my_frame, text="Dealer",bd=0)
player_frame.grid(row=0, column=0, ipadx=20)


root.mainloop()

print ("Completed my run 2342342234")
