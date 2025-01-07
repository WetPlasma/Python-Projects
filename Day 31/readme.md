# Flashcard App

This is a simple flashcard application built using Python and Tkinter. The app helps you learn French words by showing a French word on the front of the card and its English translation on the back.

## Features

- Displays a French word on the front of the card.
- Flips the card to show the English translation after 3 seconds.
- Allows you to mark words as known or unknown.
- Saves the progress of known words to a CSV file.

## Requirements

- Python 3.x
- pandas
- Tkinter (usually included with Python)

## Installation

1. Clone the repository or download the code files.
2. Ensure you have the required libraries installed. You can install pandas using pip:

    ```sh
    pip install pandas
    ```

3. Place your French words CSV file in the `data` directory with the name `french_words.csv`. The file should have two columns: `French` and `English`.

4. Ensure you have the following images in the `images` directory:
    - `card_front.png`
    - `card_back.png`
    - `wrong.png`
    - `right.png`

## Usage

1. Run the `main.py` script:

    ```sh
    python main.py
    ```

2. The flashcard window will open, displaying a French word.
3. After 3 seconds, the card will flip to show the English translation.
4. Use the buttons to mark the word as known or unknown:
    - Click the button with the cross image to mark the word as unknown.
    - Click the button with the check image to mark the word as known.

5. Known words will be saved to `data/words_to_learn.csv` and will not be shown again.

## Code Explanation

- The `nextcard` function selects a random word from the list and displays it on the card.
- The `flip_card` function flips the card to show the English translation.
- The `isknown` function removes the current word from the list of words to learn and saves the updated list to a CSV file.

## License

This project is licensed under the MIT License.
