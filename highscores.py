import tkinter as tk


class Highscores:
    def __init__(self, highscores_frame, menu_frame):
        self.highscores_frame = highscores_frame
        self.main_menu_frame = menu_frame

        self.rank_label = tk.Label(
            self.highscores_frame,
            text="Rank",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.rank_label.grid(row=0, column=0, pady=(70, 0), padx=(30, 0))

        self.name_label = tk.Label(
            self.highscores_frame,
            text="Name",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.name_label.grid(row=0, column=1, pady=(70, 0), padx=(100, 0))

        self.date_label = tk.Label(
            self.highscores_frame,
            text="Date",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.date_label.grid(row=0, column=2, pady=(80, 0), padx=(100, 0))

        self.wpm_label = tk.Label(
            self.highscores_frame,
            text="WPM",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.wpm_label.grid(row=0, column=3, pady=(80, 0), padx=(100, 0))

        self.mistakes_label = tk.Label(
            self.highscores_frame,
            text="Mistake",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 16, "bold"),
        )
        self.mistakes_label.grid(row=0, column=4, pady=(80, 0), padx=(100, 0))

        self.highscores_back_button = tk.Button(
            self.highscores_frame,
            text="Back",
            font=("arial", 16, "bold"),
            width=10,
            bg="#9C7DB8",
            command=self.open_main_menu,
        )
        self.highscores_back_button.grid(row=2, column=2, pady=(480, 0), padx=(100, 0))

    def open_main_menu(self):
        self.highscores_frame.grid_remove()
        self.main_menu_frame.grid(row=0, column=0)
