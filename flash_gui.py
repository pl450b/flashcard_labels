import tkinter as tk
import pandas as pd

class FlashcardGUI:
    def __init__(self, dataframe, label_array):
        self.dataframe = dataframe
        self.current_card = 0
        self.label_array = label_array
        self.label_stat = []

        for i in self.label_array:
            self.label_stat.append(False)

        # Create the GUI window
        self.root = tk.Tk()
        self.root.title("Flashcards")
        # Set the default window size
        window_width = 800
        window_height = 600
        self.root.geometry(f"{window_width}x{window_height}")

        # Display the flashcard question
        self.question_label = tk.Label(self.root, text=self.get_current_question(), wraplength=300)
        self.question_label.pack(pady=20)

        # show card labels
        for i in self.label_array:
            index = label_array.index(i)
            self.button = tk.Button(self.root, text=i, command=lambda index=index: self.toggle_label(index))
            self.button.pack(anchor=tk.W)

        

        # Create a button to show the answer
        self.show_answer_button = tk.Button(self.root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack(pady=10)

        # Display the flashcard answer (hidden by default)
        self.answer_label = tk.Label(self.root, text="", wraplength=300)
        self.answer_label.pack(pady=20)
        self.answer_label.config(state=tk.DISABLED)

        # Create a button to go to the next flashcard
        self.next_card_button = tk.Button(self.root, text="Next Card", command=self.next_card)
        self.next_card_button.pack(side=tk.RIGHT, padx=30)

        self.prev_card_button = tk.Button(self.root, text="Prevous Card", command=self.prev_card)
        self.prev_card_button.pack(side=tk.LEFT, padx=30)

    def get_current_question(self):
        return self.dataframe.iloc[self.current_card]['definition']     

    def get_current_answer(self):
        return self.dataframe.iloc[self.current_card]['term']

    def show_answer(self):
        answer = self.get_current_answer()
        self.answer_label.config(text=answer, state=tk.NORMAL, font=("Arial", 16))

    def next_card(self):
        self.current_card += 1

        if self.current_card >= len(self.dataframe):
            self.current_card = 0

        self.question_label.config(text=self.get_current_question(), font=("Arial", 16))
        self.answer_label.config(text="", state=tk.DISABLED)
    
    def prev_card(self):
        self.current_card -= 1

        if self.current_card <= 0:
            self.current_card = len(self.dataframe) - 1

        self.question_label.config(text=self.get_current_question(), font=("Arial", 16))
        self.answer_label.config(text="", state=tk.DISABLED)

    def toggle_label(self, label_val):
        self.label_stat[label_val] = ~(self.label_stat[label_val])
        print(self.label_stat[label_val])
        print("executed")
        self.button.config(bg="green")

    def run(self):
        self.root.mainloop()
