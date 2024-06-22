from collections import deque

# Define the goal state
goal_state = "123456780"

# Define the movements: left, right, up, down
moves = [
    (-1, 0), # Up
    (1, 0),  # Down
    (0, -1), # Left
    (0, 1)   # Right
]

# Convert a 2D list to a string
def state_to_string(state):
    return ''.join(str(num) for row in state for num in row)

# Convert a string to a 2D list
def string_to_state(string):
    return [[int(string[i * 3 + j]) for j in range(3)] for i in range(3)]

# Helper function to find the position of 0 (blank space)
def find_blank(state):
    zero_index = state.index('0')
    return zero_index // 3, zero_index % 3

# BFS Search Algorithm
def bfs_search(initial_state):
    # Queue to store the nodes
    queue = deque([(initial_state, [])])
    visited = set([initial_state])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        blank_i, blank_j = find_blank(current_state)
        for move in moves:
            new_i, new_j = blank_i + move[0], blank_j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = list(current_state)
                new_blank_index = new_i * 3 + new_j
                old_blank_index = blank_i * 3 + blank_j
                new_state[old_blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[old_blank_index]
                new_state_str = ''.join(new_state)
                if new_state_str not in visited:
                    queue.append((new_state_str, path + [new_state_str]))
                    visited.add(new_state_str)
    return None

# Function to print the puzzle state
def print_state(state):
    state_2d = string_to_state(state)
    for row in state_2d:
        print(' '.join(map(str, row)))
    print()

# Main function to solve the 8-puzzle problem
def solve_puzzle(initial_state):
    print("Initial State:")
    print_state(initial_state)
    solution_path = bfs_search(initial_state)
    if solution_path:
        print("Solution Path:")
        for step in solution_path:
            print_state(step)
    else:
        print("No solution found.")

# Function to validate user input
def validate_input(state):
    # Flatten the input and check for length and duplicates
    flat_state = [num for row in state for num in row]
    if len(flat_state) != 9:
        return False, "Input must contain exactly 9 numbers."
    if len(set(flat_state)) != 9:
        return False, "Input contains duplicate numbers."
    for num in flat_state:
        if num < 0 or num > 8:
            return False, "Numbers must be between 0 and 8 inclusive."
    return True, ""

# Function to get user input for the initial state
def get_initial_state():
    while True:
        initial_state = []
        print("Enter the initial state (3x3 grid, use 0 for the blank space):")
        for i in range(3):
            row = input(f"Enter row {i + 1}: ").split()
            if len(row) != 3:
                print("Each row must contain exactly 3 numbers. Please try again.")
                break
            try:
                row = [int(num) for num in row]
            except ValueError:
                print("All inputs must be integers. Please try again.")
                break
            initial_state.append(row)
        else:
            is_valid, message = validate_input(initial_state)
            if is_valid:
                return ''.join(str(num) for row in initial_state for num in row)
            else:
                print(f"Invalid input: {message}")

# Get the initial state from the user
initial_state = get_initial_state()

solve_puzzle(initial_state)
