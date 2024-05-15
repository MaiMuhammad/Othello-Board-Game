import tkinter as tk


class DifficultyLevelWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Choose Difficulty Level")
        self.configure(bg='sea green')
        self.difficulty = None
        self.create_window()

    # function that create the window allowing the player to choose difficulty
    def create_window(self):

        # title
        label = tk.Label(self, text="Select Difficulty", font=("Arial", 16), bg='sea green', fg='white')
        label.pack(pady=10)

        button_frame = tk.Frame(self, bg='sea green')
        button_frame.pack(pady=10)

        button_font = ("Arial", 12)
        button_bg = 'white'
        button_fg = 'grey22'

        # easy button that sets difficulty to 1
        easy_button = tk.Button(button_frame, text="Easy", font=button_font, command=lambda: self.set_difficulty_level(1), bg=button_bg, fg=button_fg)
        easy_button.pack(side=tk.LEFT, padx=10, anchor='center')

        # medium button that sets difficulty to 3
        medium_button = tk.Button(button_frame, text="Medium", font=button_font, command=lambda: self.set_difficulty_level(3), bg=button_bg, fg=button_fg)
        medium_button.pack(side=tk.LEFT, padx=10, anchor='center')

        # hard button that sets difficulty to 5
        hard_button = tk.Button(button_frame, text="Hard", font=button_font, command=lambda: self.set_difficulty_level(5), bg=button_bg, fg=button_fg)
        hard_button.pack(side=tk.LEFT, padx=10, anchor='center')

        self.protocol("WM_DELETE_WINDOW", self.destroy)

        # Set window size
        self.geometry("300x150")

    # difficulty is set and the popup is closed
    def set_difficulty_level(self, level):
        self.difficulty = level
        self.destroy()
