import tkinter as tk
import json


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
        self.highscores_frame.grid_remove()
        self.main_menu_frame.grid(row=0, column=0)

    def show_highscores(self):
        with open("highscores.json") as file:
            file_contents = file.read()

        self.highscores_list = json.loads(file_contents)

        for score in self.highscores_list:
            self.new_rank = tk.Label(
                self.highscores_frame,
                text=f"{score['rank']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_rank.grid(row=score["rank"], column=0, pady=(10, 0))

            self.new_name = tk.Label(
                self.highscores_frame,
                text=f"{score['name']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_name.grid(row=score["rank"], column=1, pady=(10, 0), padx=(100, 0))

            self.new_date = tk.Label(
                self.highscores_frame,
                text=f"{score['date']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_date.grid(row=score["rank"], column=2, pady=(10, 0), padx=(100, 0))

            self.new_wpm = tk.Label(
                self.highscores_frame,
                text=f"{score['wpm']}",
                bg="#78C0E9",
                fg="#E28596",
                font=("arial", 12, "bold"),
            )
            self.new_wpm.grid(row=score["rank"], column=3, pady=(10, 0), padx=(100, 0))

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
