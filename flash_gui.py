import tkinter as tk
import pandas as pd
import random

class FlashcardGUI:
    def __init__(self, dataframe, label_array):
        self.full_dataframe = dataframe
        self.deck_dataframe = pd.DataFrame(columns=['term', 'definition'])
        self.current_card = 0
        self.label_array = label_array
        self.label_stat = []
        self.prev_card = []

        self.label_dict = {key: "grey" for key in label_array}
        print(self.label_dict)

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
            self.button = tk.Button(self.root, text=i, command=lambda label=i: self.toggle_label(label))
            self.button.bind('<Enter>', self.enter_button)
            self.button.bind('<Leave>', self.leave_button)
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
        if self.deck_dataframe.size == 0:
            return "No cards in current deck"
        else:
            return self.deck_dataframe.iloc[self.current_card]['definition']     

    def get_current_answer(self):
        if self.deck_dataframe.size == 0:
            return "No cards in current deck"
        else:
            return self.deck_dataframe.iloc[self.current_card]['term']

    def show_answer(self):
        answer = self.get_current_answer()
        self.answer_label.config(text=answer, state=tk.NORMAL, font=("Arial", 16))

    def next_card(self):
        self.inc_card()

        self.question_label.config(text=self.get_current_question(), font=("Arial", 16))
        self.answer_label.config(text="", state=tk.DISABLED)
    
    # Fix later
    def prev_card(self):
        print("sgdgsd")
        self.dec_card()

        self.question_label.config(text=self.get_current_question(), font=("Arial", 16))
        self.answer_label.config(text="", state=tk.DISABLED)

    def inc_card(self):
        if self.current_card == len(self.deck_dataframe) - 1:
            self.current_card = 0
        else:
            self.current_card += 1
        
    def dec_card(self):
        if self.current_card == 0:
            self.current_card = len(self.deck_dataframe) - 1
        else:
            self.current_card -= 1

    # Runs every time a label is pressed in the GUI. This changes the color of the label and it's 
    # status in the lable dictionary. The current deck dataframe is also updated with each change
    def toggle_label(self, label):
        # Label dictionary update
        if(self.label_dict[label] == "grey"):
            self.label_dict[label] = "green"

        elif(self.label_dict[label] == "red"):
            self.label_dict[label] = "green"
        
        elif(self.label_dict[label] == "green"):
            self.label_dict[label] = "grey"      

        # Label button color update
        for button in self.root.winfo_children():
            if button.cget('text') == label:
                button.config(bg=self.label_dict[label])

        # Deck dataframe update
        self.deck_dataframe.drop(self.deck_dataframe.index, inplace=True)
        deck_labels = []
        for key in self.label_dict:
            if(self.label_dict[key] == "green"):
                deck_labels.append(key)

        in_deck = self.full_dataframe['labels'].str.contains('|'.join(deck_labels))
        self.deck_dataframe['term'] = self.full_dataframe.loc[in_deck, 'term']
        self.deck_dataframe['definition'] = self.full_dataframe.loc[in_deck, 'definition']
        
        # Randomize deck
        # self.deck_dataframe = self.deck_dataframe.sample(frac=1, replace=False)

    def enter_button(self, event):
        pass

    def leave_button(self, event):
        pass

    def run(self):
        self.root.mainloop()
