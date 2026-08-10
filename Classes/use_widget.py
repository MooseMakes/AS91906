# Import tkinter to initialise graphics control
import tkinter as tk

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

    def __init__(self, pad_x, pad_y, icon, icon_hover):
        # Default widget padding while idle
        self.pad_x = pad_x
        self.pad_y = pad_y
        # Increased widget padding while hovered over
        self.pad_x_hover = pad_x + 1
        self.pad_y_hover = pad_y + 1
        # Image asset assignment for hover enlargement
        self.icon = icon
        self.icon_hover = icon_hover

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
            # Increase the padding of the widget if able
            try:
                widget.configure(padding=(self.pad_x_hover, self.pad_y_hover))

            except tk.TclError:
                pass

            # Replace the image with a larger version if possible
            if hasattr(widget, "icon_hover"):
                widget.configure(image=widget.icon_hover)

    def on_leave(self, event):
        # Identify the event's origin
        widget = event.widget
        # If clicking a widget will trigger an action...
        if hasattr(widget, "invoke"):
            # Set the cursor to its default appearance
            widget.configure(cursor="")
            # Decrease the padding of the widget if able
            try:
                widget.configure(padding=(self.pad_x, self.pad_y))

            except tk.TclError:
                pass

            # If possible, replace the image with a larger version
            if hasattr(widget, "icon"):
                widget.configure(image=widget.icon)

    def on_type(self, event):
        # Play the type sound effect from assets folder on character entry
        if event.char:
            type_sound.play()
