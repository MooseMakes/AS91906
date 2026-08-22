# Import tkinter to initialise graphics control
import tkinter as tk


class Menu:
    def __init__(self, parent, root, use_widget, trigger):

        # Store root window to be referenced locally
        self.root = root
        # Store widget input logic to be referenced locally
        self.use_widget = use_widget
        # Assign the trigger page as an object to reference it locally
        self.trigger = trigger

        # Create, style, & position the current page as a subheading
        self.subheading = tk.Label(
            parent,
            text="Main menu",
            font=("Arial", 12),
            bg="#ffffff"
        )

        self.subheading.place(
            relx=0.5,
            rely=0.018,
            anchor="center"
        )

        # Create, style, & position the menu frame
        self.menu_frame = tk.Frame(
            parent,
            bg="#ffffe0",
            width=1350,
            height=600,
            relief="solid",
            borderwidth=1
        )

        self.menu_frame.place(
            relx=0.5,
            rely=0.51,
            anchor="center"
        )

        self.menu_frame.grid_propagate(False)

        self.menu_frame.columnconfigure(
            0,
            weight=1,
            uniform="column"
        )

        self.menu_frame.columnconfigure(
            1,
            weight=1,
            uniform="column"
        )

        self.menu_frame.rowconfigure(
            0,
            weight=1,
            uniform="row"
        )

        # Create, style, & position the create game button
        self.create_game = tk.Button(
            self.menu_frame,
            text="Create game",
            font=("Arial", 24),
            bg="#ffff80",
            padx=48,
            pady=12,
            command=lambda: self.trigger.load_page("create"),
            relief="solid",
            borderwidth=2
        )

        self.create_game.grid(
            row=0,
            column=0
        )

        # Create, style, & position the play game button
        self.play_game = tk.Button(
            self.menu_frame,
            text="Play game",
            font=("Arial", 24),
            bg="#ffff80",
            padx=48,
            pady=12,
            command=lambda: self.trigger.load_page("play"),
            relief="solid",
            borderwidth=2
        )

        self.play_game.grid(
            row=0,
            column=1
        )

        for widget in self.menu_frame.winfo_children():
            self.use_widget.detect_input(widget)
