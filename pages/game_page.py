import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring
from datetime import datetime
import json
import copy


class GamePage:
    def __init__(self, game_page, menu_frame, application_window, highscores_instance):
        self.game_page_frame = game_page
        self.main_menu_frame = menu_frame
        self.application_window = application_window
        self.highscores_instance = highscores_instance

        self.cpm = 0
        self.correct_characters = 0
        self.wpm = 0
        self.mistakes = 0
        self.seconds_left = 60
        self.timer_started = False
        self.text_index = 0
        self.correct_characters_indexes = set()
        self.active_timer = None

        self.timer = tk.Label(
            self.game_page_frame,
            text=self.seconds_left,
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 60, "bold"),
        )
        self.timer.grid(row=0, column=10, pady=(30, 0))

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

        self.example_text_window = tk.Text(
            self.game_page_frame,
            borderwidth=5,
            height=7,
            width=80,
            bg="#78C0E9",
            fg="#E28596",
            font=("arial", 14, "bold"),
            wrap=tk.WORD,
        )
        self.example_text_window.grid(row=2, column=0, columnspan=20)

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

        self.application_window.bind("<KeyPress>", self.key_press)

    def remove_temp_text(self, event):
        self.text_entry.delete(0, "end")

    def open_main_menu(self):
        self.game_page_frame.grid_remove()
        self.reset_game()
        self.main_menu_frame.grid(row=0, column=0)

    def key_press(self, event):
        if self.application_window.focus_get() == self.text_entry:
            self.handle_timer()
            self.check_input(event.keysym)

    def handle_timer(self):
        if not self.timer_started:
            self.timer_started = True
            self.active_timer = self.application_window.after(1000, self.lower_timer)

    def lower_timer(self):
        self.seconds_left -= 1
        self.timer.config(text=self.seconds_left)
        if self.seconds_left > 0:
            self.active_timer = self.application_window.after(1000, self.lower_timer)
        if self.seconds_left == 0:
            self.time_up()

    def check_input(self, character_pressed):
        # Get the text in the example window
        self.example_text = self.example_text_window.get("1.0", tk.END)

        # Handle user pressing spacebar
        if character_pressed == "space" and self.example_text[self.text_index] == " ":
            self.text_index += 1
            return

        # Handle user pressing backspace
        if character_pressed == "BackSpace":
            self.handle_backspace()
            return

        # Handle user pressing letters
        if character_pressed == self.example_text[self.text_index]:
            self.color_letter("green")
            if self.text_index not in self.correct_characters_indexes:
                self.correct_characters += 1
                self.correct_characters_indexes.add(self.text_index)
            self.update_cpm()
            self.update_wpm()
            self.text_index += 1
        else:
            self.color_letter("red")
            self.update_mistakes("mistake")
            self.update_cpm()
            self.update_wpm()
            self.text_index += 1

    def color_letter(self, color):
        self.example_text_window.tag_add(self.text_index, f"1.{self.text_index}")
        self.example_text_window.tag_config(self.text_index, foreground=color)

    def update_mistakes(self, reason):
        if reason == "mistake":
            self.mistakes += 1
        elif reason == "backspace":
            try:
                # get color of character we are removing
                fg = self.example_text_window.tag_cget(self.text_index, "foreground")
                if fg == "red":
                    self.mistakes -= 1
            except tk.TclError as e:
                print(f"TclError: {e}")
        self.current_mistakes.config(text=f"Mistakes: {self.mistakes}")

    def update_cpm(self):
        self.time_elapsed = 60 - self.seconds_left
        if self.time_elapsed > 0:
            self.cpm = (self.correct_characters / self.time_elapsed) * 60
            self.current_cpm.config(text=f"CPM: {int(self.cpm)}")
        else:
            self.cpm = self.correct_characters * 60
            self.current_cpm.config(text=f"CPM: {int(self.cpm)}")

    def handle_backspace(self):
        if self.text_index > 0:
            self.text_index -= 1
        self.update_mistakes("backspace")
        self.example_text_window.tag_delete(self.text_index)

    def update_wpm(self):
        self.wpm = self.cpm / 5
        self.current_wpm.config(text=f"WPM: {int(self.wpm)}")

    def time_up(self):
        messagebox.showinfo(
            "Time Up!",
            "Time is up, here are your stats:\n"
            f"Mistakes: {self.mistakes}\n"
            f"CPM: {int(self.cpm)}\n"
            f"WPM: {int(self.wpm)}\n",
        )
        self.check_highscore()
        self.open_main_menu()

    def reset_game(self):
        # Stop the timer if its active
        if self.active_timer is not None:
            self.application_window.after_cancel(self.active_timer)

        # Reset variables
        self.cpm = 0
        self.correct_characters = 0
        self.wpm = 0
        self.mistakes = 0
        self.seconds_left = 60
        self.timer_started = False
        self.text_index = 0
        self.correct_characters_indexes = set()

        # Reset labels
        self.timer.config(text=self.seconds_left)
        self.current_cpm.config(text=f"CPM: {self.cpm}")
        self.current_wpm.config(text=f"WPM: {self.wpm}")
        self.current_mistakes.config(text=f"Mistakes: {self.mistakes}")

        # Clear example_text_window
        self.example_text_window.delete("1.0", tk.END)

        # Clear text entry
        self.text_entry.delete(0, "end")

    def check_highscore(self):
        self.highscores_list = self.highscores_instance.highscores_list
        rank_15_score = self.highscores_list[14]["wpm"]
        if int(self.wpm) > rank_15_score:
            self.update_highscore()

    def update_highscore(self):
        player_name = askstring(
            "New highscore!", "You got a highscore, please enter your name"
        )
        current_datetime = datetime.now()
        formatted_day = current_datetime.strftime("%d-%m-%Y")

        for rank in self.highscores_list:
            if int(self.wpm) > rank["wpm"]:
                self.move_lower_score(rank["rank"] - 1)
                self.highscores_list[rank["rank"] - 1]["name"] = player_name
                self.highscores_list[rank["rank"] - 1]["date"] = formatted_day
                self.highscores_list[rank["rank"] - 1]["wpm"] = int(self.wpm)
                self.highscores_list[rank["rank"] - 1]["mistakes"] = self.mistakes
                with open("./data/highscores.json", "w") as outfile:
                    json.dump(self.highscores_list, outfile)
                return

    def move_lower_score(self, updated_rank):
        lower_scores = copy.deepcopy(self.highscores_list[updated_rank:-1])

        index = 0

        for score in lower_scores:
            self.highscores_list[score["rank"]]["name"] = lower_scores[index]["name"]
            self.highscores_list[score["rank"]]["date"] = lower_scores[index]["date"]
            self.highscores_list[score["rank"]]["wpm"] = lower_scores[index]["wpm"]
            self.highscores_list[score["rank"]]["mistakes"] = lower_scores[index][
                "mistakes"
            ]

            index += 1