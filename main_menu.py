import tkinter as tk


class MainMenu:
    def __init__(self, frame):
        self.frame = frame

        app_name_label = tk.Label(
            text="Typing Speed Test",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 60, "bold"),
        )
        app_name_label.grid(
            row=0, column=0, columnspan=20, padx=(70, 0), pady=(100, 200)
        )

        start_game_button = tk.Button(
            text="Start Game", bg="#70B2A5", font=("arial", 16, "bold")
        )
        start_game_button.grid(row=1, column=6)

        instructions_button = tk.Button(
            text="Instructions", bg="#9C7DB8", font=("arial", 16, "bold")
        )
        instructions_button.grid(row=1, column=11)

        high_scores_button = tk.Button(
            text="High Scores", bg="#8794d4", font=("arial", 16, "bold")
        )
        high_scores_button.grid(row=1, column=16)
