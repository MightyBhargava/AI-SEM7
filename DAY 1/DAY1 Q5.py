import matplotlib.pyplot as plt
import networkx as nx

# Define the initial state and goal state
initial_state = (3, 3, 1)  # (number of missionaries on left, number of cannibals on left, boat position)
goal_state = (0, 0, 0)  # (number of missionaries on right, number of cannibals on right, boat position)


# Function to check if a state is valid
def is_valid(state):
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # Check if missionaries are outnumbered by cannibals on either side
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False

    return True


# Function to generate valid next states
def generate_next_states(state):
    states = []
    missionaries_left, cannibals_left, boat = state

    # Possible movements of missionaries and cannibals
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    if boat == 1:  # Boat on the left side
        for move in moves:
            new_state = (missionaries_left - move[0], cannibals_left - move[1], 0)
            if is_valid(new_state):
                states.append(new_state)
    else:  # Boat on the right side
        for move in moves:
            new_state = (missionaries_left + move[0], cannibals_left + move[1], 1)
            if is_valid(new_state):
                states.append(new_state)

    return states


# Breadth-First Search algorithm to find the solution path
def bfs_search():
    queue = [(initial_state, [])]
    visited = set([initial_state])

    while queue:
        current_state, path = queue.pop(0)

        if current_state == goal_state:
            return path

        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
                visited.add(next_state)

    return None


# Function to create and plot the graph of states
def plot_solution_path(solution_path):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    for i, state in enumerate(solution_path):
        node_name = f"Step {i + 1}\n{state}"
        G.add_node(node_name)
        pos[node_name] = (i * 2, 0)
        labels[node_name] = f"Step {i + 1}"

        if i > 0:
            prev_state = solution_path[i - 1]
            edge_label = f"{prev_state} -> {state}"
            G.add_edge(f"Step {i}\n{prev_state}", node_name, label=edge_label)

    plt.figure(figsize=(12, 6))
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
    plt.title('Missionaries and Cannibals Problem Solution Path')
    plt.show()


# Solve the Missionaries and Cannibals problem
def solve_missionaries_cannibals():
    solution_path = bfs_search()

    if solution_path is None:
        print("No solution found.")
    else:
        print("Solution found:")
        for i, state in enumerate(solution_path):
            print(f"Step {i + 1}: {state}")

        plot_solution_path(solution_path)


# Run the solver
solve_missionaries_cannibals()
