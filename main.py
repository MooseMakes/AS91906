# Import tkinter to initialise graphics control
import tkinter as tk
# Import the database initialisation file
from Data.database import create_database
# Import the class containing methods used to load each page
from Classes.load_page import LoadPage

# Create the database
create_database()
# Create the root window with standard FHD resolution and a white background
root = tk.Tk()
root.geometry("1920x1080")
root.configure(bg="#ffffff")
# Load the account authentication page
load_page = LoadPage(root)
load_page.load_page("auth")
# Maintains graphical interface & receives user input with constant event loop
root.mainloop()
