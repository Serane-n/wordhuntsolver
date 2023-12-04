
# README.md for GamePigeon Word Hunt Solver

## Overview
This program is a solver for the GamePigeon Word Hunt game. It's designed for fun and educational purposes. The solver uses a trie data structure for efficient word searching and a depth-first search algorithm to find valid words on the game board.

## Prerequisites
- Python 3.x
- Text file containing a word list (`words.txt`)

## Installation
1. Clone or download the repository to your local machine.

## Adapting to Your OS
### Setting the Dictionary Path
- The program requires a path to a dictionary file (`words.txt`).
- Modify the `solver.load_dictionary()` line in the `wordhuntsolver.py` file.
    - Use backslashes (`\`) in the path for Windows.
    - Use forward slashes (`/`) for Linux, Mac, or any Unix-based OS.

    Example:
    ```python
    # For Windows
    solver.load_dictionary(r'C:\path\to\your\words.txt')

    # For Unix/Mac
    solver.load_dictionary(r'/path/to/your/words.txt')
    ```

## Usage
1. Run `wordhuntsolver.py`.
2. Enter the 16 game board letters in a left-to-right, top-down sequence when prompted.
   - Example input: 'aeagmirctoynptnl'.
   - This corresponds to the following grid:
     ```
     a e a g
     m i r c
     t o y n
     p t n l
     ```
3. The program will display the found words and execution time.

## Reporting Issues
- If you encounter any invalid words or bugs, please create an issue in the repository with the relevant details.

## Note
- This project was created out of curiosity and is not actively maintained. Dictionary updates may occur for invalid words.
- Ensure your Python environment is correctly set up and compatible with the code.

---

End of README.md
