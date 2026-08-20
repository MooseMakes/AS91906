# Import tkinter to initialise graphics control
import tkinter as tk
import sqlite3
# Import NavBar & UseWidget classes
from Classes.create_navbar import NavBar
# Import SQLite database
connect = sqlite3.connect("Data/database.db")
cursor = connect.cursor()


class Auth:

    def __init__(self, parent, root, use_widget):

        # Store root window to be referenced locally
        self.root = root
        # Store widget input logic to be referenced locally
        self.use_widget = use_widget

        # Destroy all widgets in the root window besides the page frame
        for widget in root.winfo_children():
            if widget != parent:
                widget.destroy()

        # Create, style, & position the program title as a heading
        self.heading = tk.Label(
            parent,
            text="Tutor Tower",
            font=("Arial", 48),
            bg="#ffffff"
        )

        self.heading.place(
            relx=0.5,
            rely=0.11,
            anchor="center"
        )

        # Create, style, & position the current page as a subheading
        self.subheading = tk.Label(
            parent,
            text="Account authentication",
            font=("Arial", 12),
            bg="#ffffff"
        )

        self.subheading.place(
            relx=0.5,
            rely=0.16,
            anchor="center"
        )

        # Create, style, & position the authentication frame
        self.auth_frame = tk.Frame(
            parent,
            bg="#ffffe0",
            width=580,
            height=540,
            relief="solid",
            borderwidth=1
        )

        self.auth_frame.place(
            relx=0.5,
            rely=0.58,
            anchor="center"
        )

        self.auth_frame.grid_propagate(False)

        self.auth_frame.columnconfigure(
            0,
            weight=1,
            uniform="column"
        )

        self.auth_frame.columnconfigure(
            1,
            weight=1,
            uniform="column"
        )

        self.auth_frame.rowconfigure(
            0,
            weight=1,
            uniform="row"
        )

        self.auth_frame.rowconfigure(
            1,
            weight=1,
            uniform="row"
        )

        self.auth_frame.rowconfigure(
            2,
            weight=1,
            uniform="row"
        )

        # Create, style, & position the username label
        self.username_label = tk.Label(
            self.auth_frame,
            text="Username",
            font=("Arial", 24),
            bg="#ffffe0"
        )

        self.username_label.grid(
            row=0,
            column=0
        )

        # Create, style, & position the username entry text box
        self.username_textbox = tk.Entry(
            self.auth_frame,
            font=("Arial", 24),
            width=12,
            validate="key",
            validatecommand=(
                self.root.register(self.char_limit),
                "%P",
                "12"
            )
        )

        self.username_textbox.grid(
            row=0,
            column=1
        )

        # Create, style, & position the password label
        self.password_label = tk.Label(
            self.auth_frame,
            text="Password",
            font=("Arial", 24),
            bg="#ffffe0"
        )

        self.password_label.grid(
            row=1,
            column=0
        )

        # Create, style, & position the username entry text box
        self.password_textbox = tk.Entry(
            self.auth_frame,
            font=("Arial", 24),
            width=12,
            validate="key",
            validatecommand=(
                self.root.register(self.char_limit),
                "%P",
                "12"
            )
        )

        self.password_textbox.grid(
            row=1,
            column=1
        )

        # Create, style, & position the sign up button
        self.sign_up = tk.Button(
            self.auth_frame,
            text="Sign up",
            font=("Arial", 24),
            bg="#ffff80",
            padx=48,
            width=6,
            command=lambda: self.check_error("sign_up"),
            relief="solid",
            borderwidth=2
        )

        self.sign_up.grid(
            row=2,
            column=0
        )

        # Create, style, & position the log in button
        self.log_in = tk.Button(
            self.auth_frame,
            text="Log in",
            font=("Arial", 24),
            bg="#ffff80",
            padx=48,
            width=6,
            command=lambda: self.check_error("log_in"),
            relief="solid",
            borderwidth=2
        )

        self.log_in.grid(
            row=2,
            column=1
        )

        # Detect inputs from the widgets inside the auth frame
        for widget in self.auth_frame.winfo_children():
            self.use_widget.detect_input(widget)

    def char_limit(self, text, limit):

        return len(text) <= int(limit)

    def check_error(self, target_page):

        # Store strings entered by user into text boxes
        username = self.username_textbox.get()
        password = self.password_textbox.get()

        # Check if the inputted username already exists
        cursor.execute(
            "SELECT password FROM account WHERE username = ?",
            (username,)
        )

        account_exists = cursor.fetchone()

        # Detect errors in inputted data
        if username == "" or password == "":
            self.show_error("Please enter a username and password.")

        elif target_page == "log_in":
            if not account_exists:
                self.show_error("This username doesn't exist. "
                                "You may create a new account with this "
                                "username using the sign up button.")

            # Check if the inputted password matches the inputted username
            elif password != account_exists[0]:
                self.show_error("The entered password does not match "
                                "the entered username.")

            else:
                self.prep_menu()

        elif target_page == "sign_up":
            if account_exists:
                self.show_error("This username is already in use. "
                                "You may log in to this account "
                                "with the correct password")

            else:
                # Append account details to database
                cursor.execute(
                    "INSERT INTO account (username, password) VALUES (?, ?)",
                    (username, password)
                )

                connect.commit()
                self.prep_menu()

    def show_error(self, error_msg):

        # Create the error frame
        self.error_frame = tk.Frame(
            self.auth_frame,
            bg="#ffffe0",
            relief="solid",
            borderwidth=1
        )

        self.error_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=580,
            height=540
        )

        self.error_frame.columnconfigure(
            0,
            weight=1
        )

        self.error_frame.rowconfigure(
            0,
            weight=1
        )

        self.error_frame.rowconfigure(
            1,
            weight=1
        )

        # Display the error message
        tk.Label(
            self.error_frame,
            text=error_msg,
            font=("Arial", 24),
            bg="#ffffe0",
            wraplength="480"
        ).grid(
            column=0,
            row=0
        )

        # Create cancel button & destroy error frame when pressed
        tk.Button(
            self.error_frame,
            text="Cancel",
            font=("Arial", 24),
            bg="#ffff80",
            command=self.error_frame.destroy,
            relief="solid",
            borderwidth=2,
            padx=48,
            pady=12,
            width=6
        ).grid(
            column=0,
            row=1
        )

        # Detect inputs from the widgets inside the error frame
        for widget in self.error_frame.winfo_children():
            self.use_widget.detect_input(widget)

    def prep_menu(self):

        # Re-create the navbar & load the menu page
        self.navbar = NavBar(self.root)
        self.navbar.trigger.load_page("menu")
