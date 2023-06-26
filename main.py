import pandas as pd
from flash_gui import FlashcardGUI

# Specify the path and filename of the CSV file
csv_file = 'sec_plus_deck.csv'

# Read the CSV file into a Pandas DataFrame
main_df = pd.read_csv(csv_file, delimiter='|')

label_array = []

if __name__ == "__main__":
    label_str = main_df["labels"]
    
    for i in label_str:
        split_labels = i.split(",")
        for j in split_labels:
            if j not in label_array:
                label_array.append(j)

    flashcard_gui = FlashcardGUI(main_df, label_array)
    flashcard_gui.run()
