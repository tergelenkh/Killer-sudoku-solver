import tkinter as tk
from tkinter import ttk, messagebox
from itertools import product

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Killer Sudoku Solver")
        
        # Sudoku grid
        self.grid = self.create_sudoku_grid()
        
        # Rule management UI
        self.rules = []  # Store rules as dictionaries
        self.rule_frame = ttk.Frame(root)
        self.rule_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.create_rule_ui()
        
        # Solve button
        self.solve_button = ttk.Button(self.rule_frame, text="Solve", command=self.solve_board)
        self.solve_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Restart button
        self.restart_button = ttk.Button(self.rule_frame, text="Restart", command=self.restart_board)
        self.restart_button.grid(row=3, column=1, columnspan=3, pady=10)
    
    def create_sudoku_grid(self):
        """Create a 9x9 Sudoku grid."""
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        grid = []
        for row in range(9):
            grid_row = []
            for col in range(9):
                entry = ttk.Entry(frame, width=2, justify="center", font=("Arial", 16))
                entry.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                if (row // 3 + col // 3) % 2 == 0:
                    entry.config(background="#f0f0f0")
                else:
                    entry.config(background="#ffffff")
                grid_row.append(entry)
            grid.append(grid_row)
        for i in range(9):
            frame.grid_rowconfigure(i, weight=1)
            frame.grid_columnconfigure(i, weight=1)
        return grid
    
    def create_rule_ui(self):
        """Create the UI for managing rules."""
        ttk.Label(self.rule_frame, text="Cage Constraints").grid(row=0, column=0, columnspan=3)
        
        # Add new rule fields
        self.ixs_entry = ttk.Entry(self.rule_frame, width=20)
        self.ixs_entry.grid(row=1, column=0, padx=5, pady=5)
        self.sum_entry = ttk.Entry(self.rule_frame, width=10)
        self.sum_entry.grid(row=1, column=1, padx=5, pady=5)
        add_button = ttk.Button(self.rule_frame, text="Add Rule", command=self.add_rule)
        add_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Rules list
        self.rules_list = ttk.Treeview(self.rule_frame, columns=("ixs", "sum"), show="headings", height=10)
        self.rules_list.heading("ixs", text="Cell Indices")
        self.rules_list.heading("sum", text="Sum")
        self.rules_list.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.rules_list.bind("<Double-1>", self.edit_rule)  # Double-click to edit

        # Scrollbar
        scrollbar = ttk.Scrollbar(self.rule_frame, orient="vertical", command=self.rules_list.yview)
        self.rules_list.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=2, column=3, sticky="ns")
    
    def add_rule(self):
        """Add a new rule."""
        ixs_text = self.ixs_entry.get()
        sum_text = self.sum_entry.get()
        try:
            # Parse cell indices
            ixs = eval(ixs_text)  # e.g., "[(0, 0), (0, 1), (1, 0)]"
            if not all(isinstance(ix, tuple) and len(ix) == 2 for ix in ixs):
                raise ValueError("Invalid cell indices")
            # Parse target sum
            target_sum = int(sum_text)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return
        
        # Add rule to the list
        self.rules.append({"ixs": ixs, "sum": target_sum})
        self.update_rules_list()
        self.ixs_entry.delete(0, tk.END)
        self.sum_entry.delete(0, tk.END)
    
    def update_rules_list(self):
        """Update the rules list UI."""
        for row in self.rules_list.get_children():
            self.rules_list.delete(row)
        for rule in self.rules:
            self.rules_list.insert("", "end", values=(rule["ixs"], rule["sum"]))
    
    def edit_rule(self, event):
        """Edit a selected rule from the rules list."""
        selected_item = self.rules_list.selection()
        if not selected_item:
            return
        
        # Get selected item's values
        item = self.rules_list.item(selected_item)
        values = item["values"]
        ixs, target_sum = values
        
        # Show current values in the entry fields for editing
        self.ixs_entry.delete(0, tk.END)
        self.ixs_entry.insert(0, ixs)
        self.sum_entry.delete(0, tk.END)
        self.sum_entry.insert(0, target_sum)
        
        # Remove the rule from the list to allow re-adding it
        index = self.rules_list.index(selected_item[0])
        del self.rules[index]
        self.rules_list.delete(selected_item[0])
    
    def solve_board(self):
        """Solve the Killer Sudoku puzzle."""
        board = [[self.get_cell_value(row, col) for col in range(9)] for row in range(9)]
        if self.solve_sudoku(board):
            self.update_grid_with_solution(board)
        else:
            messagebox.showerror("Error", "No solution found")
    
    def get_cell_value(self, row, col):
        """Get the value of a cell, default to 0 if empty."""
        val = self.grid[row][col].get()
        return int(val) if val.isdigit() else 0
    
    def update_grid_with_solution(self, solution):
        """Update the Sudoku grid with the solved values."""
        for row in range(9):
            for col in range(9):
                self.grid[row][col].delete(0, tk.END)
                self.grid[row][col].insert(0, str(solution[row][col]))

    def restart_board(self):
        """Clear all numbers in the Sudoku grid."""
        for row in range(9):
            for col in range(9):
                self.grid[row][col].delete(0, tk.END)
    
    def solve_sudoku(self, board):
        """Solve the Sudoku using backtracking with constraints."""
        def is_valid(board, row, col, num):
            """Check if placing num at (row, col) is valid."""
            # Row and column constraints
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
            
            # 3x3 subgrid constraints
            subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
            for i, j in product(range(subgrid_row, subgrid_row + 3), range(subgrid_col, subgrid_col + 3)):
                if board[i][j] == num:
                    return False
            
            # Cage constraints
            for rule in self.rules:
                if (row, col) in rule["ixs"]:
                    total = num
                    for (r, c) in rule["ixs"]:
                        if (r, c) != (row, col):
                            total += board[r][c]
                    if total > rule["sum"]:
                        return False
                    if 0 not in [board[r][c] for (r, c) in rule["ixs"]] and total != rule["sum"]:
                        return False
            return True
        
        def backtrack():
            """Backtracking algorithm."""
            for row, col in product(range(9), range(9)):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = 0
                    return False
            return True
        
        return backtrack()

# Run the application
root = tk.Tk()
app = SudokuApp(root)
root.mainloop()
