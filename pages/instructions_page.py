import tkinter as tk


class InstructionsPage:
    """
    Represents the instructions page of the Typing Speed Test application.

    Attributes
    ----------
    instructions_frame(tk.Frame): The frame for displaying instructions.
    main_menu_frame(tk.Frame): The main menu frame.
    test_label(tk.Label): A label displaying instructions for using the typing speed test app.
    back_button(tk.Button): A button to navigate back to the main menu.
    """

    def __init__(self, instruction_frame, menu_frame):
        """
        Initializes the InstructionsPage class.

        Parameters
        ----------
        instruction_frame(tk.Frame): The frame for displaying instructions.
        menu_frame(tk.Frame): The main menu frame.
        """
        self.instructions_frame = instruction_frame
        self.main_menu_frame = menu_frame
        self.test_label = tk.Label(
            self.instructions_frame,
            text="This app lets you test your typing speed. \n When you start "
            "the game you will receive a list of random words. \n You will "
            "get 60 seconds to type as much as you can. \n The app will keep "
            "track of all correct characters you typed. \n At the end you "
            "will see how many Character per minute (CPM), \n and words per "
            "minutes (WPM) you typed. \n It will also give you the amount of "
            "mistakes you made. \n Plus give you the option to enter your "
            "name if you got a highscore.",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 18, "bold"),
        )
        self.test_label.grid(
            row=0, column=0, columnspan=20, padx=(40, 0), pady=(100, 60)
        )

        self.back_button = tk.Button(
            self.instructions_frame,
            text="Back",
            font=("arial", 16, "bold"),
            width=10,
            bg="#9C7DB8",
            command=self.open_main_menu,
        )
        self.back_button.grid(row=1, column=10)

    def open_main_menu(self):
        """
        Switches to the main menu frame and hides the instructions frame.
        """
        self.instructions_frame.grid_remove()
        self.main_menu_frame.grid(row=0, column=0)
