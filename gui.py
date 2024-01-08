import tkinter as tk


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
        self.master.config(padx=20, pady=20, bg="#8794d4")
        self.master.minsize(height=700, width=900)
