import tkinter as tk
from main_menu import MainMenu
from instructions_page import InstructionsPage


class TypingSpeedTest:
    """
    Creates the GUI for the speed typing test app.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.
    """

    def __init__(self, master):
        """
        Initializes the TypingSpeedTest class.

        Parameters
        ----------
        master(tk.Tk): The main Tkinter window.
        """
        self.master = master
        self.master.title("Typing Speed Test")
        self.master.config(padx=20, pady=20, bg="#78C0E9")
        self.master.minsize(height=700, width=900)

        # Main menu frame
        self.main_menu_frame = tk.Frame(self.master, bg="#78C0E9")
        self.main_menu_frame.grid(row=0, column=0)

        # Instructions frame
        self.instructions_frame = tk.Frame(self.master, bg="#78C0E9")

        # Main menu instance
        self.main_menu = MainMenu(self.main_menu_frame, self.instructions_frame)

        # Instructions instance
        self.instructions_page = InstructionsPage(
            self.instructions_frame, self.main_menu_frame
        )
