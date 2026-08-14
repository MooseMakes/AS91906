# Import tkinter to initialise graphics control
import tkinter as tk
# Import classes from UI files to call initialisation methods
from UI.account import Account
from UI.authentication import Auth
from UI.create_quiz import Create
from UI.menu import Menu
from UI.play_quiz import Play
from UI.settings import Settings
from UI.shop import Shop
from UI.stats import Stats
from UI.support import Support


'''
The LoadPage class controls how frames and widgets are
displayed across pages.
'''


class LoadPage:

    def __init__(self, root):

        # Root window assignment
        self.root = root
        # Assign a parent frame to the current widgets below the navbar
        self.page_frame = tk.Frame(
            root,
            bg="#ffffff"
        )
        # Position the frame to fill the entire non-navbar window space
        self.page_frame.pack(
            fill="both",
            expand=True
        )

    def check_exit(self, trigger_button):

        # Check if the user is attempting to exit the game or app
        if trigger_button == "exit":
            exit_msg = "Are you sure you want to exit the application?"
            action = self.root.destroy
            self.confirm_exit(exit_msg, action)

        elif self.page == "play":
            exit_msg = "Are you sure you want to exit the current game?"
            # Assign an anonymous function
            action = lambda: self.load_page(trigger_button)
            self.confirm_exit(exit_msg, action)

        else:
            self.load_page(trigger_button)

    def confirm_exit(self, action, exit_msg):

        # Create the confirmation frame
        exit_frame = tk.Frame(
            self.page_frame,
            bg="#ffffc0"
        )
        exit_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        # Display the exit message
        tk.Label(
            exit_frame,
            text=exit_msg,
            font=("Arial", 18),
            bg="#ffffc0"
        ).pack(
            padx=9,
            pady=9
        )
        # Create cancel button & destroy exit frame when pressed
        tk.Button(
            exit_frame,
            text="Cancel",
            font=("Arial", 12),
            bg="#ffff80",
            command=exit_frame.destroy
        ).pack(
            side="left",
            padx=9,
            pady=9
        )
        # Create confirmation button & call action when pressed
        tk.Button(
            exit_frame,
            text="Confirm",
            font=("Arial", 12),
            bg="#ffff80",
            command=action
        ).pack(
            side="left",
            padx=9,
            pady=9
        )

    def load_page(self, trigger_button):

        # Destroy all non-navbar widgets and children widgets
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Load the page the user is trying to reach
        if trigger_button == "account":
            Account(self.page_frame)

        elif trigger_button == "auth":
            Auth(self.page_frame)

        elif trigger_button == "create":
            Create(self.page_frame)

        elif trigger_button == "menu":
            Menu(self.page_frame)

        elif trigger_button == "play":
            Play(self.page_frame)

        elif trigger_button == "settings":
            Settings(self.page_frame)

        elif trigger_button == "shop":
            Shop(self.page_frame)

        elif trigger_button == "stats":
            Stats(self.page_frame)

        elif trigger_button == "support":
            Support(self.page_frame)
