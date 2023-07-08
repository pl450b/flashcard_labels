# Welcome to Wesley's Flashcards Tool!
This is a fun tool for practicing and organizing your own flashcards deck

Once running, click the label buttons on the left side to select the cards you want to appear
in your current study session. Everytime you select/deselect a label, the current deck is updated and
randomized.
### Keyboard Shortcuts
Next Card: right arrow\
Previous Card: left arrow\
Show Answer: Down arrow
## Installation
1. Clone the direction using ```git clone https://github.com/pl450b/smart_flashcards```
2. Install required packages using ```pip install -r requirements.txt```
3. Now just put your flashcard CSV into this directory and you are ready to go!
## Usage
```python3 main.py <your_deck.csv>```
That's it!
## CSV Decks
This program uses csv files to get the flashcards for the program. The csv files are organized as 
follows:
```term|definition|labels```
- `term`: what you will have to guess
- `definition`: the text on the "front" side of the flashcard
- `labels`: a list of labels (seperated by commas) used to organize the deck and select which cards to study

Check out the `example_deck.csv` to create you own, and `sec_plus_deck.csv` for my current set of Security+ flashcards.
   
*Score feature comming soon!*
