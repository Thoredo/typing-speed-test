import tkinter as tk
import json


class Highscores:
    """
    Represents the high scores page of the Typing Speed Test application.

    Attributes
    ----------
    highscores_frame(tk.Frame): The frame for displaying high scores.
    main_menu_frame(tk.Frame): The main menu frame.
    rank_label(tk.Label): A label indicating the rank column.
    name_label(tk.Label): A label indicating the name column.
    date_label(tk.Label): A label indicating the date column.
    wpm_label(tk.Label): A label indicating the words per minute (WPM) column.
    mistakes_label(tk.Label): A label indicating the mistakes column.
    highscores_back_button(tk.Button): A button to navigate back to the main menu.
    highscores_list(list): A list containing high scores loaded from the 'highscores.json' file.
    ranking_widgets(list): A list to store widgets displaying high scores dynamically.
    """

    def __init__(self, highscores_frame, menu_frame):
        """
        Initializes the Highscores class.

        Parameters
        ----------
        highscores_frame(tk.Frame): The frame for displaying high scores.
        menu_frame(tk.Frame): The main menu frame.
        """
        self.highscores_frame = highscores_frame
        self.main_menu_frame = menu_frame

        self.rank_label = tk.Label(
            self.highscores_frame,
            text="Rank",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.rank_label.grid(row=0, column=0, pady=(10, 0), padx=(30, 0))

        self.name_label = tk.Label(
            self.highscores_frame,
            text="Name",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.name_label.grid(row=0, column=1, pady=(10, 0), padx=(100, 0))

        self.date_label = tk.Label(
            self.highscores_frame,
            text="Date",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.date_label.grid(row=0, column=2, pady=(10, 0), padx=(100, 0))

        self.wpm_label = tk.Label(
            self.highscores_frame,
            text="WPM",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.wpm_label.grid(row=0, column=3, pady=(10, 0), padx=(100, 0))

        self.mistakes_label = tk.Label(
            self.highscores_frame,
            text="Mistakes",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.mistakes_label.grid(row=0, column=4, pady=(10, 0), padx=(100, 0))

        self.highscores_back_button = tk.Button(
            self.highscores_frame,
            text="Back",
            font=("arial", 16, "bold"),
            width=10,
            bg="#9C7DB8",
            command=self.open_main_menu,
        )
        self.highscores_back_button.grid(row=16, column=2, pady=(20, 0), padx=(100, 0))

        self.show_highscores()

    def open_main_menu(self):
        """
        Switches to the main menu frame and hides the high scores frame.
        """
        self.highscores_frame.grid_remove()
        self.main_menu_frame.grid(row=0, column=0)

    def show_highscores(self):
        """
        Loads high scores from 'highscores.json' and dynamically displays them on the high scores frame.
        """
        with open("./data/highscores.json") as file:
            file_contents = file.read()

        self.highscores_list = json.loads(file_contents)

        self.ranking_widgets = []

        # Create labels for all 15 scores, and add widgets to self.ranking_widgets
        # to easily reset them when needed.
        for score in self.highscores_list:
            self.new_rank = tk.Label(
                self.highscores_frame,
                text=f"{score['rank']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_rank.grid(row=score["rank"], column=0, pady=(10, 0))
            self.ranking_widgets.append(self.new_rank)

            self.new_name = tk.Label(
                self.highscores_frame,
                text=f"{score['name']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_name.grid(row=score["rank"], column=1, pady=(10, 0), padx=(100, 0))
            self.ranking_widgets.append(self.new_name)

            self.new_date = tk.Label(
                self.highscores_frame,
                text=f"{score['date']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_date.grid(row=score["rank"], column=2, pady=(10, 0), padx=(100, 0))
            self.ranking_widgets.append(self.new_date)

            self.new_wpm = tk.Label(
                self.highscores_frame,
                text=f"{score['wpm']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_wpm.grid(row=score["rank"], column=3, pady=(10, 0), padx=(100, 0))
            self.ranking_widgets.append(self.new_wpm)

            self.new_mistakes = tk.Label(
                self.highscores_frame,
                text=f"{score['mistakes']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_mistakes.grid(
                row=score["rank"], column=4, pady=(10, 0), padx=(100, 0)
            )
            self.ranking_widgets.append(self.new_mistakes)

    def clear_rank_widgets(self):
        """
        Clears the dynamically displayed ranking widgets on the high scores frame.
        """
        for widget in self.ranking_widgets:
            widget.destroy()
