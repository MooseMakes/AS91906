# Import tkinter to initialise graphics control
import tkinter as tk
# Import the database initialisation file
from Data.database import create_database
# Import the initial page, Authentication
from UI.authentication import Auth

# Create the database
create_database()
# Create the root window with standard FHD resolution
root = tk.Tk()
root.geometry("1920x1080")

# Create & position the parent frame
parent = tk.Frame(
    root,
    bg="#ffffff"
    )

parent.pack(
    fill="both",
    expand=True
)

# Load the account authentication page
Auth(parent, root)
# Maintains graphical interface & receives user input with constant event loop
root.mainloop()
