# Import tkinter to initialise graphics control
import tkinter as tk


'''
The LoadPage class controls how frames and widgets are
displayed across pages.
'''


class LoadPage:

    def __init__(self, root, use_widget):

        # Root window assignment
        self.root = root
        # Widget input control assignment
        self.use_widget = use_widget

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

    def check_exit(self, target_page):

        # Check if the user is attempting to exit the game or app
        if target_page == "exit":
            exit_msg = "Are you sure you want to exit the application?"
            action = self.root.destroy
            self.confirm_exit(exit_msg, action)

        elif self.page == "play":
            exit_msg = "Are you sure you want to exit the current game?"
            # Assign an anonymous function
            action = lambda: self.load_page(target_page)  # noqa: E731
            self.confirm_exit(exit_msg, action)

        else:
            self.load_page(target_page)

    def confirm_exit(self, exit_msg, action):

        # Create the confirmation frame
        exit_frame = tk.Frame(
            self.page_frame,
            bg="#ffffe0"
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
            font=("Arial", 12),
            bg="#ffffe0"
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

    def load_page(self, target_page):

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

        # Destroy all non-navbar widgets and children widgets
        for widget in self.page_frame.winfo_children():
            widget.destroy()

        # Load the page the user is trying to reach
        if target_page == "account":
            Account(self.page_frame, self.use_widget)

        elif target_page == "auth":
            Auth(self.page_frame, self.root, self.use_widget, self)

        elif target_page == "create":
            Create(self.page_frame, self.use_widget)

        elif target_page == "menu":
            Menu(self.page_frame, self.use_widget)

        elif target_page == "play":
            Play(self.page_frame, self.use_widget)

        elif target_page == "settings":
            Settings(self.page_frame, self.use_widget)

        elif target_page == "shop":
            Shop(self.page_frame, self.use_widget)

        elif target_page == "stats":
            Stats(self.page_frame, self.use_widget)

        elif target_page == "support":
            Support(self.page_frame, self.use_widget)

        # Make the target page that was triggered the current page
        self.page = target_page
