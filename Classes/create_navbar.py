# Import tkinter to initialise graphics control
import tkinter as tk
# Import Python Imaging Library
from PIL import Image, ImageTk


'''
The NavBar class creates, styles, and positions the navigation bar
frame and the buttons inside. It also calls methods from the LoadPage
class, which allows buttons to load a new page when invoked.
'''


class NavBar:

    def __init__(self, root, use_widget, trigger):

        # Assign UseWidget as an object to reference it locally
        self.use_widget = use_widget
        # Assign the trigger page as an object to reference it locally
        self.trigger = trigger
        # Assign the icon assets to both pillow and photo images
        self.support_pillow = Image.open("Assets/support.png").resize((96, 96))
        self.support_icon = ImageTk.PhotoImage(self.support_pillow)
        self.stats_pillow = Image.open("Assets/stats.png").resize((96, 96))
        self.stats_icon = ImageTk.PhotoImage(self.stats_pillow)
        self.shop_pillow = Image.open("Assets/shop.png").resize((96, 96))
        self.shop_icon = ImageTk.PhotoImage(self.shop_pillow)
        self.settings_pillow = Image.open("Assets/settings.png").resize((96, 96))  # noqa: E501
        self.settings_icon = ImageTk.PhotoImage(self.settings_pillow)
        self.account_pillow = Image.open("Assets/account.png").resize((96, 96))
        self.account_icon = ImageTk.PhotoImage(self.account_pillow)
        self.exit_pillow = Image.open("Assets/exit.png").resize((96, 96))
        self.exit_icon = ImageTk.PhotoImage(self.exit_pillow)

        # Navbar frame assignment and styling
        self.frame = tk.Frame(
            root,
            bg="#ffffff"
        )

        # Icon button assignment
        self.support_button = tk.Button(
            self.frame,
            image=self.support_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("support"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        self.stats_button = tk.Button(
            self.frame,
            image=self.stats_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("stats"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        self.shop_button = tk.Button(
            self.frame,
            image=self.shop_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("shop"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        self.settings_button = tk.Button(
            self.frame,
            image=self.settings_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("settings"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        self.account_button = tk.Button(
            self.frame,
            image=self.account_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("account"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        self.exit_button = tk.Button(
            self.frame,
            image=self.exit_icon,
            bg="#ffffff",
            command=lambda: self.trigger.check_exit("exit"),
            relief="flat",
            borderwidth=0,
            width=108,
            height=108
        )

        # Menu button assignment
        self.menu_button = tk.Button(
            self.frame,
            text="Tutor Tower",
            font=("Arial", 24),
            bg="#ffff80",
            command=lambda: self.trigger.check_exit("menu"),
            relief="solid",
            borderwidth=2,
            padx=48,
            pady=12,
            width=27
        )

        # Navbar frame positioning
        self.frame.pack(
            side="top",
            fill="x",
            before=self.trigger.page_frame
        )

        # Icon button positioning
        self.support_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.stats_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.shop_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.menu_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.settings_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.account_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        self.exit_button.pack(
            side="left",
            padx=12,
            pady=12
        )

        # Assign the image objects to be referenced in the buttons
        self.support_button.pillow = self.support_pillow
        self.support_button.icon = self.support_icon
        self.stats_button.pillow = self.stats_pillow
        self.stats_button.icon = self.stats_icon
        self.shop_button.pillow = self.shop_pillow
        self.shop_button.icon = self.shop_icon
        self.settings_button.pillow = self.settings_pillow
        self.settings_button.icon = self.settings_icon
        self.account_button.pillow = self.account_pillow
        self.account_button.icon = self.account_icon
        self.exit_button.pillow = self.exit_pillow
        self.exit_button.icon = self.exit_icon

        # Detect inputs from the widgets inside the navbar frame
        for widget in self.frame.winfo_children():
            self.use_widget.detect_input(widget)
