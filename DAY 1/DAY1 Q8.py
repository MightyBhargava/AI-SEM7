import matplotlib.pyplot as plt
from collections import deque

# Define grid dimensions
ROWS = 5
COLS = 5

# Define grid with obstacles (1: obstacle, 0: empty space)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

# Define possible movements (up, down, left, right)
movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        if current not in visited:
            visited.add(current)

            for move in movements:
                neighbor = (current[0] + move[0], current[1] + move[1])

                if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS:
                    if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0:
                        stack.append(neighbor)
                        parent[neighbor] = current

    # Trace back the path from goal to start
    path = []
    if goal in parent:
        step = goal
        while step is not None:
            path.append(step)
            step = parent[step]
        path = path[::-1]

    return path


def plot_grid(start, goal, path):
    fig, ax = plt.subplots(figsize=(ROWS, COLS))

    # Plot grid and obstacles
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, ROWS - 1 - i), 1, 1, color='gray'))

    # Plot start and goal points
    ax.text(start[1] + 0.5, ROWS - 1 - start[0] + 0.5, 'Start', ha='center', va='center', fontsize=12, color='blue')
    ax.text(goal[1] + 0.5, ROWS - 1 - goal[0] + 0.5, 'Goal', ha='center', va='center', fontsize=12, color='green')

    # Plot DFS path
    if path:
        for i in range(len(path) - 1):
            ax.plot([path[i][1] + 0.5, path[i + 1][1] + 0.5],
                    [ROWS - 1 - path[i][0] + 0.5, ROWS - 1 - path[i + 1][0] + 0.5], color='orange', linewidth=2)

    # Customize plot
    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title('Depth-First Search (DFS) Visualization')

    plt.show()


# Define start and goal points
start_point = (0, 0)
goal_point = (4, 4)

# Perform DFS and get the path
path_found = dfs(start_point, goal_point)

# Visualize the grid, start, goal, and path
plot_grid(start_point, goal_point, path_found)
