import sys
from flash_gui import FlashcardGUI

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <your_deck.csv>")
    else:
        csv_file = sys.argv[1]
        flashcard_gui = FlashcardGUI(csv_file)
        flashcard_gui.run()
