# Card Spark 

## Table of Contents 
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Examples](#examples)
5. [Supported File Format](#supported-file-format)
6. [How to Load a File](#how-to-load-a-file)
7. [Contributing](#contributing)
8. [License](#license)


## Introduction 
Card Spark is a flashcard app designed to spark you learning journey. Whether you are mastering new concepts, studying for exams, or improving your memory, Card Spark makes it easy to create, navigate, and learn at your own pace.

## Requirements 
- Python 3.x installed on your system 

## Usage 
1. Clone the repository
2. Open terminal or command prompt and navigate to the project directory 
3. Run the application 
```
python3 CardSpark.py
```
4. Follow on screen prompts to create, review and manage flashcards 

## Examples
```
Main Menu
1. Create a new deck
2. Load a deck
3. Exit
Enter your choice: 1

Enter name for the deck: deck1

Actions Menu
1. Add a flashcard
2. Delete a flashcard
3. Learn and study your flashcards
4. Test yourself, take a quiz
5. Display all flashcards
6. Go to Main Menu

Enter your choice: 1

Enter the question: What is the capital of France?

Enter the answer: Paris
Flashcards saved successfully
```
## Supported File Format 
CardSpark allows you to load flashcards from a `.txt` file. To ensure the file is loaded correctly, it must follow this format:

- Each flashcard must be written in this format 
```
Q:[Question] A:[Answer]
```
- Flashcards are not be separated by a blank line 
- Each flashcard must be written in one line

Example
```
Q: What is the capital of France  A: Paris  
Q: What colour is the sky A: Blue 
Q: What is 2 + 2 A: 4
```
## How to Load a File 

1. Select the `Load a Deck` option from the main menu
2. Enter the name of the `.txt` file without the file extension 
- Example: if your file is `deck1.txt` then enter `deck1` when prompted  

## Contributing 
1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Submit a pull request with a clear description of your changes

## License 
[MIT](https://choosealicense.com/licenses/mit/)