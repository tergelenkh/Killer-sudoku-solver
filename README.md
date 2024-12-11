# Killer Sudoku Solver with Tkinter

The Killer Sudoku Solver with Tkinter is a GUI-based application designed to assist users in solving Killer Sudoku puzzles. [Killer Sudoku](https://en.wikipedia.org/wiki/Killer_sudoku) is a variation of the classic [Sudoku](https://en.wikipedia.org/wiki/Sudoku_code) game, where players must fill a 9x9 grid with numbers 1-9, ensuring that each number appears exactly once in every row, column, and 3x3 subgrid. Additionally, the grid contains "cages" with predefined sums, and the numbers in each cage must add up to the specified sum without repetition.

This project allows users to:

* Input custom Sudoku puzzles directly into a 9x9 editable grid.
* Define custom rules for cages by specifying the cell indices and their target sums.
* Solve the puzzle using a backtracking algorithm that respects Sudoku and cage constraints.
* Reset the grid to start fresh with a new puzzle.
The application is built with Python's Tkinter library for the graphical interface and incorporates a robust solving algorithm to handle most valid Killer Sudoku setups. It provides a user-friendly way to interact with the puzzle, add constraints, and solve even complex configurations.

## Features

- Editable 9x9 Sudoku grid.
- Rule creation and management for custom cages.
- Solve button to compute the solution.
- Restart button to clear the grid.
- Real-time validation of cage constraints during solving.

## Used Technologies

- Python 3.x
- Tkinter (for GUI)
- Backtracking algorithm (for solving the puzzle)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the project folder.
4. Run the script using Python: `python killer_sudoku_solver.py`.
5. Enjoy solving your Killer Sudoku puzzles!

## Usage/Examples

1. **Inputting Grid Values**:
   - Click any cell in the 9x9 Sudoku grid and type a number (1-9). Leave cells blank for unsolved values.

2. **Adding Cage Constraints**:
   - Use the "Cell Indices" input field to specify the cells in the cage, in the format: `[(row, col), (row, col), ...]`.
     - Example: `[(0,0), (0,1), (1,0)]` for a cage that includes the top-left 2x2 grid.
   - Use the "Sum" input field to specify the target sum for that cage.
   - Click "Add Rule" to save the cage constraint.

3. **Editing Cage Constraints**:
   - Double-click any rule in the "Cage Constraints" list to edit it. Modify the cell indices or target sum, then re-add the rule.

4. **Solving the Puzzle**:
   - Once all constraints and known values are entered, click "Solve" to compute the solution.
   - The grid will update with the solved values if a valid solution exists.

5. **Restarting the Grid**:
   - To clear the grid and start fresh, click the "Restart" button.

### Visual example how to use:

<img width="400" alt="Screenshot 2024-12-11 at 7 35 39 PM" src="https://github.com/user-attachments/assets/f79c6a78-0bac-450f-bd9f-659987d91998">

Let's solve this sudoku
<img width="400">![IMG_8517](https://github.com/user-attachments/assets/96a4d14e-e84b-4f75-9cf1-dacf0abff2e5)

Use the "Cell Indices" input field to specify the cells in the cage
<img width="400" alt="Screenshot 2024-12-11 at 8 23 31 PM" src="https://github.com/user-attachments/assets/31794508-1ee2-42bd-bfa2-58d6d8c79227">

Complete the cell cages
<img width="400" alt="Screenshot 2024-12-11 at 8 46 20 PM" src="https://github.com/user-attachments/assets/67df7097-3ebd-44e3-93dc-aa36b10cf43d">

After clicking solve button here is the result.
<img width="400" alt="Screenshot 2024-12-11 at 8 48 13 PM" src="https://github.com/user-attachments/assets/a41b5bdb-04e2-40a9-aeff-7abe6c75ebd8">

Checking if it is correct.
<img width="400">![IMG_8518](https://github.com/user-attachments/assets/b3357685-6d09-4f20-9fc9-7f05f2b569c2)

### Notes:
- The rows and columns are zero-indexed: `(0,0)` corresponds to the top-left cell, `(8,8)` to the bottom-right.
- Ensure the cage constraints are valid; overlapping cells or invalid sums may result in no solution.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements
The inspiration for this project stems from my personal passion for playing Sudoku. As someone who has always found joy in solving puzzles, I wanted to explore the game further and create something unique that blends my interest in Killer Sudoku with new ideas. By working on this project, I aim to deepen my understanding of the game.

[Constraint satisfaction problem](https://medium.com/my-udacity-ai-nanodegree-notes/solving-sudoku-think-constraint-satisfaction-problem-75763f0742c9) Helped me to understand deeply how to solve killer sudoku.

[Solving sudoku puzzles with computer | Killer sudoku rules](https://www.youtube.com/watch?v=-Jlh5E5U-rg&list=PLbfxO23TgNPi4mKMsCb18g27PBSxkM5vC&index=4) Youtube video to solve killer sudoku using javascript.

[Killer sudoku combination cheat sheet](https://www.griddlers.net/images/KakuroCheatSheet.pdf) All of the possible combinations that using in killer sudoku.

[Algorithm to Solve Sudoku | Sudoku Solver](https://www.geeksforgeeks.org/sudoku-backtracking-7/) An OG sudoku solving source codes using different methods.

[Killer sudoku online solver](https://imois.in/posts/sudoku-solver/) Got an idea from here how to implement cages from user.

Used [readme.so](https://readme.so/editor) to write this Readme.md file
