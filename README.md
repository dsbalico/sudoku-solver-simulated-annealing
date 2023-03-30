# Sudoku Solver using Simulated Annealing

This is a Python class `SudokuSolverAnnealing` that uses the Simulated Annealing algorithm to solve Sudoku puzzles. The `SudokuSolverAnnealing` class takes a 9x9 list representing a Sudoku board and returns a solution to the puzzle. The algorithm also accepts optional parameters to control its behavior, including the maximum number of iterations, initial temperature, and cooling rate.

## Installation
This project requires Python 3.6 or higher. To use the SudokuSolverAnnealing class, simply copy the code into your project or import it as a module.

## Usage
The `SudokuSolverAnnealing` class is used to solve Sudoku puzzles using the Simulated Annealing algorithm. To use it, first create an instance of the class with a 9x9 list representing a Sudoku board, and optionally set any desired parameters. Then, call the solve method on the instance to obtain a solution to the puzzle.

    from SudokuSolverAnnealing import SudokuSolverAnnealing
    
    # Define a Sudoku board as a 9x9 list. 
    board = [[0,0,0,0,8,0,9,6,2],
	     	 [0,0,8,5,1,0,0,0,0],
	    	 [0,6,0,0,9,0,1,0,0],
	   	 [0,8,4,1,6,9,7,0,3],
	    	 [3,0,0,7,0,0,2,1,0],
	  	 [0,0,7,0,2,0,4,0,0],
	      	 [0,0,1,2,7,5,6,4,0],
	     	 [0,7,2,9,0,0,0,0,1],
	     	 [5,4,0,6,0,0,8,0,0]]

	# Create an instance of the SudokuSolverAnnealing class and solve the puzzle.
	solver = SudokuSolverAnnealing(board)
	solution = solver.solve_sudoku()
	
	# Print the solution.
	solver.print_sudoku(solution)

The code above defines a Sudoku board as a 9x9 list and passes it to an instance of the `SudokuSolverAnnealing` class. The `solve_sudoku` method is then called on the instance to obtain a solution to the puzzle. Finally, the `print_sudoku` method is used to print the solution to the console.

## Parameters
The `SudokuSolverAnnealing` class accepts the following parameters:

- `board` (list): A 9x9 list representing the Sudoku board. The board should contain integers or 0 to represent empty cells.
- `max_iteration` (int): The maximum number of iterations the algorithm will perform before stopping. Default is 100000.
- `initial_temperature` (float): The initial temperature for the simulated annealing algorithm. Default is 0.6.
- `cooling_rate` (float): The rate at which the temperature decreases during the simulated annealing algorithm. Default is 0.999.

## Contributing
If you want to contribute to this project, there are several ways you can do so:

1.  Submit bugs and feature requests: If you find a bug or have a feature request, please submit an issue on the GitHub repository.
2.  Submit pull requests: If you have a fix or improvement for the code, feel free to submit a pull request on the GitHub repository. Please make sure your code is well-documented and tested.
3.  Spread the word: If you like this project, please share it with your friends and colleagues.
