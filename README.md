# Welcome to Wesley's Flashcards Tool!
This is a fun tool for practicing and organizing you own flashcards deck
## Instalation
1. Clone the direction using ```git clone https://github.com/pl450b/smart_flashcards```
2. Install required packages using ```pip install -r requirements.txt```
3. Now just put your flashcard CSV into this directory and you are ready to go!
## Usage
```python3 main.py <your_deck.csv>```
That's it!
## CSV Decks
This program uses csv files to get the flashcards for the program. The csv files
are organized as follows:
```term|definition|labels```
- `term`: what you will have to guess
- `definition`: the text on the "front" side of the flashcard
- `labels`: a list of labels (seperated by commas) used to organize the deck and select which cards to study
*Score feature comming soon!*
