import random
import math

class SudokuSolverAnnealing:
    """ Solving Sudoku puzzles using the Simulated Annealing algorithm. """

    def __init__(self, board, max_iteration=100000, initial_temperature=0.6, cooling_rate=0.999):
        """
        Parameters:
        - board (list): A 9x9 list representing the Sudoku board. The board should contain integers or 0 to represent empty cells.
        - max_iteration (int): The maximum number of iterations the algorithm will perform before stopping.
        - initial_temperature (float): The initial temperature for the simulated annealing algorithm.
        - cooling_rate (float): The rate at which the temperature decreases during the simulated annealing algorithm.
        """
        self.max_iteration = max_iteration
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate

        self.empty_cells = self.get_all_empty_cells(board)
        self.initial_board = self.initialize_sudoku_board(board)

    def print_sudoku(self, board):
        """ Displays Sudoku Board """
        
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def get_all_empty_cells(self, board):
        """ Returns a list of tuples representing the positions of all empty cells on the board.

        Parameters:
        - board (list): A 2D list representing the Sudoku board. The board must contain integers or 0 to represent empty cells.
    
        Returns:
        - A list of tuples representing the positions of all empty cells on the board. Each tuple contains two integers (y, x)
          representing the row and column indices of the empty cell, respectively. """

        empty_cells = []

        for y, row in enumerate(board):
            for x in range(len(row)):
                if board[y][x] == 0:
                    empty_cells.append((y, x))

        return empty_cells
    
    def get_list_cost(self, arr):
        """ Calculates the cost of a list based on the number of repeated elements.

        Parameters:
        - arr (list): A list of elements to be evaluated for repetition cost.
            
        Returns:
        - An integer representing the cost of repeated elements in the input list. """
        cost = 0
        size = len(arr)
        
        for i in range(size): # Iterate through each element in the list
            for j in range(i + 1, size): # Iterate through each subsequent element in the list
                if arr[i] == arr[j]: # If there is a repeated element
                    cost += 1 # Increment the cost by 1

        return cost

    def get_sudoku_cost(self, board):
        """ Calculates the cost of a Sudoku board based on the number of repeated numbers in each row, column, and sub-grid.
        
        Parameters:
        - board (list): A 2D list representing the Sudoku board. It should have 9 rows and 9 columns. Each element should be an integer between 0 and 9 (inclusive), where 0 represents an empty cell.
            
        Returns:
        - An integer representing the cost of repeated numbers in the input Sudoku board. The cost is calculated by counting the number of times a number is repeated in each row, column, and sub-grid of the board. The higher the cost, the more incorrect the solution is. """
        cost = 0
        
        # Iterate over each row in the board.
        for y, row in enumerate(board):
            cost += self.get_list_cost(row)
        
        # Iterate over each column in the board.
        for x in range(9):
            col = [board[y][x] for y in range(9)]
            cost += self.get_list_cost(col)
        
        # Iterate over each sub-grid in the board.
        for i in range(3):
            for j in range(3):
                subgrid = [board[y][x] for y in range(i*3, (i+1)*3) for x in range(j*3, (j+1)*3)]
                cost += self.get_list_cost(subgrid)
        
        return cost
    
    def initialize_sudoku_board(self, board):
        """ Initializes a Sudoku board by filling in the empty cells with random numbers that do not repeat within their respective rows.

        Parameters:
        - board (list): A 9x9 list representing the Sudoku board. 
        
        Returns:
        - list: A new 2D list representing the initialized Sudoku board. """

        # Create a copy of the input board to avoid modifying the original board.
        new_board = [row[:] for row in board]

        for y, row in enumerate(board):
            numbers = [] # List to hold numbers in the row.

            # Get all current numbers in the row
            for x, col in enumerate(row):
                if col != 0:
                    numbers.append(col)

            # Iterate over each column in the row.
            for x, col in enumerate(row):
                if col == 0: # Check if cell is empty.
                    while True: # Keep generating numbers until we find one that's valid.
                        candidate = random.randint(1, 9) # Generate a random candidate number.

                        if candidate not in numbers: # Check if candidate number is not in current row.
                            new_board[y][x] = candidate # Set the cell to the candidate number.
                            numbers.append(candidate) # Add the candidate number to the list of current numbers.

                            break

        return new_board
    
    def generate_neighbor(self, board):
        """ Generates a new neighbor state by randomly choosing 2 empty cells and swapping them.
        
        Parameters:
        - board (list): A 9x9 list representing the Sudoku board.

        Returns:
        - 2D list: A new neighbor state of the input board with two randomly chosen empty cells swapped. """

        # make a copy of the board
        new_board = [row[:] for row in board]  

        # choose two empty cells at random
        cell1, cell2 = random.sample(self.empty_cells, 2)

        # swap their values
        new_board[cell1[0]][cell1[1]], new_board[cell2[0]][cell2[1]] = new_board[cell2[0]][cell2[1]], new_board[cell1[0]][cell1[1]]  
        
        return new_board
    
    def solve_sudoku(self):
        """ Runs the simulated annealing algorithm to solve a Sudoku puzzle.

        Returns:
        - If a solution is found: the solved Sudoku board.
        - If no solution is found: the latest state of the Sudoku board after reaching the maximum iteration limit.
        
        Algorithm:
        1. Make a copy of the initial board and set it as the current state.
        2. Calculate the cost of the current state.
        3. Set the current temperature to the initial temperature and the iteration count to 0.
        4. While the iteration count is less than the maximum iteration:
            a. If the current state is the solution, return it.
            b. Generate a new state by generating a new neighbor.
            c. Calculate the cost of the new state.
            d. Calculate the delta cost between the new state and the current state.
            e. If the new state has a lower cost, set it as the current state.
            f. If the new state has a higher cost, calculate the acceptance probability and 
            decide whether to accept the new state based on the probability.
            g. Increment the iteration count and decrease the temperature.
        5. If the algorithm reaches the maximum iteration, return the latest state of the board. """

        # make a copy of the board
        current_state = [row[:] for row in self.initial_board]

        # Get the cost of the initial board
        current_cost = self.get_sudoku_cost(current_state)

        current_temperature = self.initial_temperature
        iteration = 0

        print("\nSolving Sudoku board...\n")

        while iteration < self.max_iteration:
            # Sudoku is solved if the current cost is 0
            if current_cost == 0:
                print("\nSudoku solved!\n")
                print(f"Iterations: {iteration}\nTemperature: {current_temperature}\n")
                
                return current_state

            # Generate a new state by generating a new neighbor
            new_state = self.generate_neighbor(current_state)

            # Take the cost of the newly generated neighbor
            new_cost = self.get_sudoku_cost(new_state)

            delta_cost = new_cost - current_cost
            
            # Means the new cost is less than the current cost
            if delta_cost < 0:
                current_state = [row[:] for row in new_state]
                current_cost = new_cost
            else:
                # If the new cost is greater than the current cost, calculate the probability that program will accept it
                acceptance_probability = math.exp(-delta_cost / current_temperature)
                
                if random.random() < acceptance_probability:
                    current_state = [row[:] for row in new_state]
                    current_cost = new_cost

            iteration += 1

            # Decrease the temperature
            current_temperature = current_temperature * self.cooling_rate

        print(f"\nSudoku not solved after {iteration} tries. Please Try Again...\nSudoku board may be invalid or you need to update my parameters.\n")
        
        return current_state