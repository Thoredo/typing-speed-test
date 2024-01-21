import tkinter as tk
from pages.main_menu import MainMenu
from pages.instructions_page import InstructionsPage
from pages.game_page import GamePage
from pages.highscores import Highscores


class TypingSpeedTest:
    """
    Creates the GUI for the speed typing test app.

    Attributes
    ----------
    master (tk.Tk): The main Tkinter window.

    Frames
    -------
    main_menu_frame: Frame containing the main menu options.
    instructions_frame: Frame displaying typing instructions.
    game_page_frame: Frame for the active typing game.
    highscores_frame: Frame displaying highscores.

    Instances
    -------
    highscores_instance: An instance of the Highscores class, managing
        highscores display and interactions.
    game_page: An instance of the GamePage class, handling the active
        typing game and interactions.
    main_menu: An instance of the MainMenu class, providing the main menu
        options and navigation.
    instructions_page: An instance of the InstructionsPage class,
        displaying typing instructions.
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

        # Active game frame
        self.game_page_frame = tk.Frame(self.master, bg="#78C0E9")

        # Highscores frame
        self.highscores_frame = tk.Frame(self.master, bg="#78C0E9")

        # Higscores instance
        self.highscores_instance = Highscores(
            self.highscores_frame, self.main_menu_frame
        )

        # Game Page instance
        self.game_page = GamePage(
            self.game_page_frame,
            self.main_menu_frame,
            self.master,
            self.highscores_instance,
        )

        # Main menu instance
        self.main_menu = MainMenu(
            self.main_menu_frame,
            self.instructions_frame,
            self.game_page_frame,
            self.game_page,
            self.highscores_frame,
            self.highscores_instance,
        )

        # Instructions instance
        self.instructions_page = InstructionsPage(
            self.instructions_frame, self.main_menu_frame
        )
