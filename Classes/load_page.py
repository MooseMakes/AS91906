# Import tkinter to initialise graphics control
import tkinter as tk


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

    # TO DO

    def check_exit(self, trigger_button):

        if trigger_button == "exit":
            exit_msg = "Are you sure you want to exit the application?"
            action = self.root.destroy
            self.confirm_exit(exit_msg, action)

        elif self.page == "play":
            exit_msg = "Are you sure you want to exit the current game?"
            action = lambda: self.load_page(trigger_button)
            self.confirm_exit(exit_msg, action)

        else:
            self.load_page(trigger_button)

    # TO DO

    def confirm_exit(self, action, exit_msg):

        exit_frame = tk.Frame(
            self.page_frame,
            bg="#ffffc0"
        )
        exit_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        tk.Label(
            exit_frame,
            text=exit_msg,
            font=("Arial", 18),
            bg="#ffffc0"
        ).pack(
            padx=9,
            pady=9
        )
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

    # TO DO

    def load_page(self, trigger_button):

        for widget in self.page_frame.winfo_children():
            widget.destroy()

        if trigger_button == "account":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "auth":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "create":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "menu":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "play":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "settings":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "shop":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "stats":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION

        elif trigger_button == "support":
            pass  # PLACEHOLDER: UI/(PAGE).py CONNECTION
