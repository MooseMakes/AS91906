# Import tkinter to initialise graphics control
import tkinter as tk
# Import the initial page, Authentication
from UI.authentication import Auth

# Create the root window with standard FHD resolution
root = tk.Tk()
root.geometry("1920x1080")
# Create the parent frame
parent = tk.Frame(root)
# Load the account authentication page
Auth(parent, root)
# Maintains graphical interface & receives user input with constant event loop
root.mainloop()
