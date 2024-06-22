import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Define the capacities of the jugs
capacity_a = 4
capacity_b = 3

# Define the goal amount of water to measure
goal_amount = 2

# Initial state of the jugs (both empty)
initial_state = (0, 0)


# Breadth-first search algorithm to find the solution path
def bfs_search():
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        current_state, path = queue.popleft()
        if current_state[0] == goal_amount or current_state[1] == goal_amount:
            return path

        # Generate all possible next states
        next_states = []

        # Fill jug A
        next_states.append((capacity_a, current_state[1]))

        # Fill jug B
        next_states.append((current_state[0], capacity_b))

        # Empty jug A
        next_states.append((0, current_state[1]))

        # Empty jug B
        next_states.append((current_state[0], 0))

        # Pour from A to B
        pour_amount = min(current_state[0], capacity_b - current_state[1])
        next_states.append((current_state[0] - pour_amount, current_state[1] + pour_amount))

        # Pour from B to A
        pour_amount = min(current_state[1], capacity_a - current_state[0])
        next_states.append((current_state[0] + pour_amount, current_state[1] - pour_amount))

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))
                visited.add(state)

    return None


# Function to plot the state of the jugs
def plot_jug_state(state, action):
    plt.figure(figsize=(10, 6))

    # Plot Jug A
    plt.bar(1, state[0], width=0.4, align='center', alpha=0.5, color='blue', label='Jug A')

    # Plot Jug B
    plt.bar(2, state[1], width=0.4, align='center', alpha=0.5, color='green', label='Jug B')

    plt.xticks([1, 2], ['Jug A', 'Jug B'])
    plt.ylabel('Capacity')
    plt.title(f'Action: {action}')
    plt.ylim(0, max(capacity_a, capacity_b) + 1)
    plt.legend()
    plt.grid(True)
    plt.show()


# Solve the water jug problem
def solve_water_jug_problem():
    solution_path = bfs_search()

    if solution_path is None:
        print("No solution found.")
        return

    print("Solution Path:")
    print(initial_state)
    for i, state in enumerate(solution_path):
        action = f"Step {i + 1}: {state}"
        print(action)
        plot_jug_state(state, action)


# Run the solver
solve_water_jug_problem()
