# Import tkinter to initialise graphics control
import tkinter as tk
# Import Python Imaging Library
from PIL import ImageTk
# Import pygame to initialise audio control
import pygame
pygame.mixer.init()
# Sound effect asset assignment
click_sound = pygame.mixer.Sound("Assets/click.wav")
hover_sound = pygame.mixer.Sound("Assets/hover.mp3")
type_sound = pygame.mixer.Sound("Assets/type.mp3")


'''
The UseWidget class contains functions used for determining
widgets' attributes upon user interaction
'''


class UseWidget:

    def detect_input(self, widget):

        # Bind user inputs to methods
        widget.bind("<Button-1>", self.on_click)
        widget.bind("<Enter>", self.on_hover)
        widget.bind("<Leave>", self.on_leave)

        # Bind key presses if the widget is a text box
        if isinstance(widget, tk.Entry):
            widget.bind("<Key>", self.on_type)

    def on_click(self, event):

        # Identify the event's origin and allow it to recieve keyboard inputs
        widget = event.widget
        widget.focus_set()

        # If clicking a widget will trigger an action...
        if hasattr(widget, "invoke"):
            # Play the click sound effect from the assets folder
            click_sound.play()

    def on_hover(self, event):

        # Identify the event's origin
        widget = event.widget

        # If clicking a widget will trigger an action...
        if hasattr(widget, "invoke"):
            # Play the hover sound effect from the assets folder
            hover_sound.play()
            # Allow the widget to receive keyboard inputs
            widget.configure(cursor="hand2")

            # If possible, increase the size of the icon
            if hasattr(widget, "pillow"):
                widget.icon_hover = ImageTk.PhotoImage(
                    widget.pillow.resize((108, 108))
                )

                widget.configure(image=widget.icon_hover)

            # If possible, increase the padding of the button
            else:
                try:
                    pad_x = widget.cget("padx")
                    pad_y = widget.cget("pady")

                    widget.configure(
                        padx=pad_x + 6,
                        pady=pad_y + 6
                    )

                except tk.TclError:
                    pass

    def on_leave(self, event):

        # Identify the event's origin
        widget = event.widget

        # If clicking a widget will trigger an action...
        if hasattr(widget, "invoke"):
            # Set the cursor to its default appearance
            widget.configure(cursor="")

            # If possible, decrease the size of the icon
            if hasattr(widget, "icon"):
                widget.configure(image=widget.icon)

            # If possible, decrease the padding of the button
            else:
                try:
                    pad_x = widget.cget("padx")
                    pad_y = widget.cget("pady")
                    widget.configure(padx=pad_x - 6, pady=pad_y - 6)

                except tk.TclError:
                    pass

    def on_type(self, event):

        # Play the type sound effect from assets folder on character entry
        if event.char:
            type_sound.play()
