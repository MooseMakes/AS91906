# Import tkinter to initialise graphics control
import tkinter as tk
# Import the database initialisation file
from Data.database import create_database
# Import the class used to load each page
from Classes.load_page import LoadPage
# Import the class used to register widget inputs
from Classes.use_widget import UseWidget
# Import the class used to load the navbar
from Classes.create_navbar import NavBar

# Create the database
create_database()
# Create the root window with standard FHD resolution and a white background
root = tk.Tk()
root.geometry("1920x1080")
root.configure(bg="#ffffff")
# Load the menu page
use_widget = UseWidget()
load_page = LoadPage(root, use_widget)
navbar = NavBar(root, use_widget, load_page)
load_page.load_page("menu")
# Maintains graphical interface & receives user input with constant event loop
root.mainloop()
