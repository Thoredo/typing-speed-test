import tkinter as tk
import sys

sys.path.insert(1, "./data/")

from data.word_generator import WordGenerator


class MainMenu:
    def __init__(
        self,
        menu_frame,
        instructions_frame,
        game_frame,
        game_instance,
        highscores_frame,
        highscores_instance,
    ):
        self.main_menu_frame = menu_frame
        self.instructions_frame = instructions_frame
        self.active_game_frame = game_frame
        self.game_instance = game_instance
        self.highscores_frame = highscores_frame
        self.highscores_instance = highscores_instance

        app_name_label = tk.Label(
            self.main_menu_frame,
            text="Typing Speed Test",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 60, "bold"),
        )
        app_name_label.grid(
            row=0, column=0, columnspan=20, padx=(70, 0), pady=(100, 200)
        )

        start_game_button = tk.Button(
            self.main_menu_frame,
            text="Start Game",
            bg="#70B2A5",
            font=("arial", 16, "bold"),
            width=10,
            command=self.start_game,
        )
        start_game_button.grid(row=1, column=6)

        instructions_button = tk.Button(
            self.main_menu_frame,
            text="Instructions",
            bg="#9C7DB8",
            font=("arial", 16, "bold"),
            command=self.open_instructions,
            width=10,
        )
        instructions_button.grid(row=1, column=11)

        high_scores_button = tk.Button(
            self.main_menu_frame,
            text="High Scores",
            bg="#8794d4",
            font=("arial", 16, "bold"),
            width=10,
            command=self.open_highscores,
        )
        high_scores_button.grid(row=1, column=16)

    def open_instructions(self):
        self.main_menu_frame.grid_remove()
        self.instructions_frame.grid(row=0, column=0)

    def start_game(self):
        self.main_menu_frame.grid_remove()
        self.change_example_text()
        self.active_game_frame.grid(row=0, column=0)

    def fill_word_list(self):
        final_string = ""
        word_generator = WordGenerator()
        for _ in range(100):
            new_word = word_generator.add_word()
            final_string = final_string + new_word + " "
        return final_string

    def change_example_text(self):
        new_example_text = self.fill_word_list()
        self.game_instance.example_text_window.config(state=tk.NORMAL)
        self.game_instance.example_text_window.delete("1.0", tk.END)
        self.game_instance.example_text_window.insert(
            tk.END,
            new_example_text,
        )
        self.game_instance.example_text_window.config(state=tk.DISABLED)

    def open_highscores(self):
        self.main_menu_frame.grid_remove()
        self.highscores_instance.clear_rank_widgets()
        self.highscores_instance.show_highscores()
        self.highscores_frame.grid(row=0, column=0)
