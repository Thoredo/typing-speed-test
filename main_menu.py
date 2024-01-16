import tkinter as tk


class MainMenu:
    def __init__(self, menu_frame, instructions_frame, game_frame):
        self.main_menu_frame = menu_frame
        self.instructions_frame = instructions_frame
        self.active_game_frame = game_frame

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
        )
        high_scores_button.grid(row=1, column=16)

    def open_instructions(self):
        self.main_menu_frame.grid_remove()
        self.instructions_frame.grid(row=0, column=0)

    def start_game(self):
        self.main_menu_frame.grid_remove()
        self.active_game_frame.grid(row=0, column=0)
