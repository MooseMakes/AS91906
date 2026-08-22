# Import tkinter to initialise graphics control
import tkinter as tk


class Menu:
    def __init__(self, parent, use_widget):

        # Store widget input logic to be referenced locally
        self.use_widget = use_widget

        # Create, style, & position the current page as a subheading
        self.subheading = tk.Label(
            parent,
            text="Main menu",
            font=("Arial", 12),
            bg="#ffffff"
        )

        self.subheading.place(
            relx=0.5,
            rely=0.02,
            anchor="center"
        )
