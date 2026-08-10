# Import tkinter to initialise graphics control
import tkinter as tk
# Import the class containing methods used to load each page
from load_page import LoadPage

'''
The NavBar class creates and positions the navigation bar buttons
'''


class NavBar:

    def __init__(self, root):
        #
        self.frame = tk.Frame(root)
        # Icon asset assignment
        self.support_icon = tk.PhotoImage(file="Assets/support.png")
        self.stats_icon = tk.PhotoImage(file="Assets/stats.png")
        self.shop_icon = tk.PhotoImage(file="Assets/shop.png")
        self.settings_icon = tk.PhotoImage(file="Assets/settings.png")
        self.account_icon = tk.PhotoImage(file="Assets/account.png")
        self.exit_icon = tk.PhotoImage(file="Assets/exit.png")
        #
        self.support_button = tk.Button(
            self.frame,
            image=self.support_icon,
            command=lambda: LoadPage.load_support()
        )
        #
        self.stats_button = tk.Button(
            self.frame,
            image=self.stats_icon,
            command=lambda: LoadPage.load_stats()
        )
        #
        self.shop_button = tk.Button(
            self.frame,
            image=self.shop_icon,
            command=lambda: LoadPage.load_shop()
        )
        #
        self.settings_button = tk.Button(
            self.frame,
            image=self.settings_icon,
            command=lambda: LoadPage.load_settings()
        )
        #
        self.account_button = tk.Button(
            self.frame,
            image=self.account_icon,
            command=lambda: LoadPage.load_account()
        )
        #
        self.exit_button = tk.Button(
            self.frame,
            image=self.exit_icon,
            command=lambda: LoadPage.load_exit()
                )
        #
        self.menu_button = tk.Button(
            self.frame,
            text="Tutor Tower",
            font=("Arial", 18),
            bg="#ffffc0",
            pad_x="PLACEHOLDER",
            pad_y="PLACEHOLDER",
            command=lambda: LoadPage.load_menu()
                )
