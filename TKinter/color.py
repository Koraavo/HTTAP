import tkinter as tk

application_window = tk.Tk()

from tkinter import colorchooser

rgb_color, web_color = colorchooser.askcolor(parent=application_window,
                                             initialcolor=(255, 0, 0))