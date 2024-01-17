import tkinter as tk


class GamePage:
    def __init__(self, game_page, menu_frame, application_window):
        self.game_page_frame = game_page
        self.main_menu_frame = menu_frame
        self.application_window = application_window
        self.cpm = 0
        self.correct_characters = 0
        self.wpm = 0
        self.mistakes = 0
        self.seconds_left = 60
        self.timer_started = False
        self.text_index = 0
        self.correct_characters_indexes = set()

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
        self.main_menu_frame.grid(row=0, column=0)

    def key_press(self, event):
        if self.application_window.focus_get() == self.text_entry:
            self.handle_timer()
            self.check_input(event.keysym)

    def handle_timer(self):
        if not self.timer_started:
            self.timer_started = True
            self.application_window.after(1000, self.lower_timer)

    def lower_timer(self):
        self.seconds_left -= 1
        self.timer.config(text=self.seconds_left)
        if self.seconds_left > 0:
            self.application_window.after(1000, self.lower_timer)

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
            self.text_index += 1
        else:
            self.color_letter("red")
            self.update_mistakes("mistake")
            self.update_cpm()
            self.text_index += 1

    def color_letter(self, color):
        self.example_text_window.tag_add(self.text_index, f"1.{self.text_index}")
        self.example_text_window.tag_config(self.text_index, foreground=color)

    def update_mistakes(self, reason):
        if self.text_index == 0:
            return
        if reason == "mistake":
            self.mistakes += 1
        elif reason == "backspace":
            try:
                # get color of character we are removing
                fg = self.example_text_window.tag_cget(self.text_index, "foreground")
                if fg == "red":
                    self.mistakes -= 1
            except tk.TclError as e:
                print(f"TclError: {e}, 'spacebar' getting removed")
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
