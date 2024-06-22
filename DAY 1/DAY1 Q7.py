from collections import deque


def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for move in movements:
            neighbor = (current[0] + move[0], current[1] + move[1])

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
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


def main():
    # Input grid dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Input grid values
    print("Enter the grid values (0 for empty space, 1 for obstacles):")
    grid = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Each row should have {cols} values.")
            return
        grid.append(row)

    # Input start and goal points
    start = tuple(map(int, input("Enter the start point (row col): ").split()))
    goal = tuple(map(int, input("Enter the goal point (row col): ").split()))

    # Perform BFS and get the path
    path_found = bfs(grid, start, goal)

    # Output the path found
    if path_found:
        print(f"Shortest path from {start} to {goal}:")
        print(path_found)
    else:
        print(f"No path found from {start} to {goal}.")


if __name__ == "__main__":
    main()
