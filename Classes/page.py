# Import tkinter and ttk to initialise graphics control
import tkinter as tk
# ttk is a modern Tkinter API that adapts widget appearance to OS
# from tkinter import ttk

# Import pygame to initialise audio control
import pygame
pygame.mixer.init()

# Default widget padding while idle
pad_x = "TO DO: Value assignment"
pad_y = "TO DO: Value assignment"

# Increased widget padding while hovered over
pad_x_hover = "TO DO: Value assignment"
pad_y_hover = "TO DO: Value assignment"

# Image asset assignment for hover enlargement
img = "TO DO: Asset assignment"
img_hover = "TO DO: Asset assignment"


'''
The Page class contains functions used for both creating widgets
and determining their properties and attributes upon user interaction
'''


class Page:

    def on_click(self, event):
        # Identify the event's origin
        widget = event.widget
        # Play the click sound effect from the assets folder
        pygame.mixer.Sound("Assets/click.wav").play()
        # Allow the widget to receive keyboard inputs
        widget.focus_set()

        # Trigger the widget's action if able
        if hasattr(widget, "invoke"):
            widget.invoke()

    def on_hover(self, event):
        # Identify the event's origin
        widget = event.widget
        # Play the hover sound effect from the assets folder
        pygame.mixer.Sound("Assets/hover.mp3").play()
        # Allow the widget to receive keyboard inputs
        widget.configure(cursor="hand2")
        # Increase the padding of the widget if able
        try:
            widget.configure(padding=(pad_x_hover, pad_y_hover))
        except tk.TclError:
            pass
        # Replace the image with a larger version if possible
        if hasattr(widget, img_hover):
            widget.configure(image=widget.img_hover)

    def on_leave(self, event):
        # Identify the event's origin
        widget = event.widget
        # Set the cursor to its default appearance
        widget.configure(cursor="")
        # Decrease the padding of the widget if able
        try:
            widget.configure(padding=(pad_x, pad_y))
        except tk.TclError:
            pass
        # Replace the image with a larger version if possible
        if hasattr(widget, img):
            widget.configure(image=widget.img)

    def on_type(self, event):
        # Play the type sound effect from assets folder on character entry
        if event.char:
            pygame.mixer.Sound("Assets/type.mp3").play()

    def create_button(self):
        pass

    def create_toggle(self):
        pass

    def create_slider(self):
        pass

    def create_dropdown(self):
        pass

    def create_textinput(self):
        pass
