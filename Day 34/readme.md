# Quiz App

This project is a GUI-based Quiz Application built with Python using the `tkinter` library. It fetches trivia questions from the Open Trivia Database (https://opentdb.com/) and allows users to answer true/false questions while keeping track of their score.

## Features

- **Dynamic Question Loading**: Questions are fetched from an online API, ensuring variety every time the app is run.
- **User Feedback**: Visual feedback is provided (green/red background) based on the correctness of the user's answer.
- **Score Tracking**: The app keeps track of and displays the user's score in real-time.
- **Simple and Clean UI**: Built using `tkinter` for a straightforward user experience.

## File Structure

```plaintext
|-- data.py            # Handles fetching questions from the Open Trivia Database
|-- main.py            # Entry point for the application
|-- question_model.py  # Defines the Question class
|-- quiz_brain.py      # Contains the logic for handling quiz questions
|-- ui.py              # Manages the graphical user interface
```

## Requirements

To run this application, ensure you have the following installed:

- Python 3.7 or higher
- Required Python packages:
  - `requests`
  - `tkinter` (usually comes pre-installed with Python)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd quiz-app
   ```

2. Install dependencies:

   ```bash
   pip install requests
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## How It Works

1. **Fetching Questions**: The app retrieves questions using the Open Trivia Database API in `data.py`.
2. **Question Logic**: The `QuizBrain` class in `quiz_brain.py` handles the logic for moving between questions and checking answers.
3. **GUI**: The `QuizInterface` class in `ui.py` manages the user interface, showing the questions and processing user input.

## How to Use

1. Launch the app using the instructions above.
2. Read the question displayed on the screen.
3. Click the **True** or **False** button based on your answer.
4. Observe the background color for feedback:
   - **Green**: Correct answer
   - **Red**: Incorrect answer
5. Continue answering questions until the quiz ends.
6. At the end, your final score will be displayed.

## API Source

This application fetches questions from the [Open Trivia Database API](https://opentdb.com/).

## Screenshots

(Include screenshots of the application if possible, showing its interface and features.)

## Future Improvements

- Add support for multiple-choice questions.
- Include different categories and difficulty levels for users to select.
- Save scores locally or in a database for tracking user performance.
- Improve the UI design with modern libraries like `customtkinter` or `PyQt`.



