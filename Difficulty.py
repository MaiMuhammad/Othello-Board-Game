import tkinter as tk

class DifficultyLevelWindow(tk.Tk):
    def __init__(self, set_difficulty_level_callback):
        super().__init__()
        self.title("Choose Difficulty Level")
        self.configure(bg='sea green')
        self.set_difficulty_level_callback = set_difficulty_level_callback
        self.difficulty = None
        self.create_window()

    def create_window(self):
        label = tk.Label(self, text="Select Difficulty", font=("Arial", 16), bg='sea green', fg='white')
        label.pack(pady=10)

        button_frame = tk.Frame(self, bg='sea green')
        button_frame.pack(pady=10)

        button_font = ("Arial", 12)
        button_bg = 'white'
        button_fg = 'grey22'

        easy_button = tk.Button(button_frame, text="Easy", font=button_font, command=lambda: self.set_difficulty_level(1), bg=button_bg, fg=button_fg)
        easy_button.pack(side=tk.LEFT, padx=10, anchor='center')

        medium_button = tk.Button(button_frame, text="Medium", font=button_font, command=lambda: self.set_difficulty_level(3), bg=button_bg, fg=button_fg)
        medium_button.pack(side=tk.LEFT, padx=10, anchor='center')

        hard_button = tk.Button(button_frame, text="Hard", font=button_font, command=lambda: self.set_difficulty_level(5), bg=button_bg, fg=button_fg)
        hard_button.pack(side=tk.LEFT, padx=10, anchor='center')

        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Set window size
        self.geometry("300x150")

    def set_difficulty_level(self, level):
        self.difficulty = level
        self.set_difficulty_level_callback(self.difficulty)
        self.destroy()

if __name__ == "__main__":
    def on_difficulty_selected(difficulty):
        return difficulty

    difficulty_window = DifficultyLevelWindow(on_difficulty_selected)
    difficulty_window.mainloop()