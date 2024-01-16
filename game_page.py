import tkinter as tk


class GamePage:
    def __init__(self, game_page, menu_frame):
        self.game_page_frame = game_page
        self.main_menu_frame = menu_frame
        self.cpm = 0
        self.wpm = 0
        self.mistakes = 0
        self.seconds_left = 60

        self.timer = tk.Label(
            self.game_page_frame,
            text=f"{self.seconds_left}",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 60, "bold"),
        )
        self.timer.grid(row=0, column=10, pady=(30,0))

        self.current_cpm = tk.Label(
            self.game_page_frame,
            text=f"CPM: {self.cpm}",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 14, "bold"),
        )
        self.current_cpm.grid(row=1, column=5, pady=(100, 10))

        self.current_wpm = tk.Label(
            self.game_page_frame,
            text=f"WPM: {self.wpm}",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 14, "bold"),
        )
        self.current_wpm.grid(row=1, column=10, pady=(100, 10))

        self.current_mistakes = tk.Label(
            self.game_page_frame,
            text=f"Mistakes: {self.mistakes}",
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 14, "bold"),
        )
        self.current_mistakes.grid(row=1, column=15, pady=(100, 10))

        self.example_text = tk.Text(
            self.game_page_frame,
            borderwidth=5,
            height=7,
            width=80,
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 14, "bold"),
            wrap=tk.WORD,
        )
        self.example_text.insert(
            tk.END,
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        )
        self.example_text.config(state=tk.DISABLED)
        self.example_text.grid(row=2, column=0, columnspan=20)

        self.text_entry = tk.Entry(
            self.game_page_frame,
            width=80,
        )
        self.text_entry.insert(0, "Enter your text here:")
        self.text_entry.grid(row=3, column=0, columnspan=20, pady=20)
        self.text_entry.bind("<FocusIn>", self.remove_temp_text)

        self.game_back_button = tk.Button(
            self.game_page_frame,
            text="Back",
            font=("arial", 16, "bold"),
            width=10,
            bg="#9C7DB8",
            command=self.open_main_menu,
        )
        self.game_back_button.grid(row=4, column=10)

    def remove_temp_text(self, event):
        self.text_entry.delete(0, "end")

    def open_main_menu(self):
        self.game_page_frame.grid_remove()
        self.main_menu_frame.grid(row=0, column=0)
