# Import tkinter to initialise graphics control
import tkinter as tk
# Import the class containing methods used to load each page
from load_page import LoadPage


'''
The NavBar class creates, styles, and positions the navigation bar frame
and the buttons inside. It also calls methods from the LoadPage class,
which allows buttons to load a new page when invoked.
'''


class NavBar:

    def __init__(self, root):
        # Icon asset assignment
        self.support_icon = tk.PhotoImage(file="Assets/support.png")
        self.stats_icon = tk.PhotoImage(file="Assets/stats.png")
        self.shop_icon = tk.PhotoImage(file="Assets/shop.png")
        self.settings_icon = tk.PhotoImage(file="Assets/settings.png")
        self.account_icon = tk.PhotoImage(file="Assets/account.png")
        self.exit_icon = tk.PhotoImage(file="Assets/exit.png")
        # Navbar frame assignment and styling
        self.frame = tk.Frame(
            root,
            bg="#ffff80"
            )
        # Icon button assignment
        self.support_button = tk.Button(
            self.frame,
            image=self.support_icon,
            command=lambda: LoadPage.load_support()
        )
        self.stats_button = tk.Button(
            self.frame,
            image=self.stats_icon,
            command=lambda: LoadPage.load_stats()
        )
        self.shop_button = tk.Button(
            self.frame,
            image=self.shop_icon,
            command=lambda: LoadPage.load_shop()
        )
        self.settings_button = tk.Button(
            self.frame,
            image=self.settings_icon,
            command=lambda: LoadPage.load_settings()
        )
        self.account_button = tk.Button(
            self.frame,
            image=self.account_icon,
            command=lambda: LoadPage.load_account()
        )
        self.exit_button = tk.Button(
            self.frame,
            image=self.exit_icon,
            command=lambda: LoadPage.load_exit()
                )
        # Menu button assignment
        self.menu_button = tk.Button(
            self.frame,
            text="Tutor Tower",
            font=("Arial", 18),
            bg="#ffffc0",
            command=lambda: LoadPage.load_menu()
                )
        # Navbar frame positioning
        self.frame.pack(
                side="top",
                fill="x"
                )
        # Icon button positioning
        self.support_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.stats_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.shop_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.menu_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.settings_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.account_button.pack(
            side="left",
            padx=9,
            pady=9
        )
        self.exit_button.pack(
            side="left",
            padx=9,
            pady=9
        )
