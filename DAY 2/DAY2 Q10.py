from heapq import heappop, heappush

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start node
        self.h = 0  # Heuristic to goal node
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.position)

def a_star_algorithm(start, end, graph):
    def heuristic(node1, node2):
        # Using Manhattan distance as heuristic
        return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

    open_list = []
    closed_list = set()

    start_node = Node(start)
    end_node = Node(end)

    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)
        closed_list.add(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        x, y = current_node.position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next_position in neighbors:
            if (next_position[0] < 0 or next_position[0] >= len(graph) or
                next_position[1] < 0 or next_position[1] >= len(graph[0]) or
                graph[next_position[0]][next_position[1]] == 1):
                continue

            neighbor = Node(next_position, current_node)
            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heappush(open_list, neighbor)

    return None

def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g > node.g:
            return False
    return True

def main():
    rows = int(input("Enter the number of rows in the grid: "))
    cols = int(input("Enter the number of columns in the grid: "))

    graph = []
    print("Enter the grid row by row (0 for free cell, 1 for obstacle):")
    for _ in range(rows):
        row = list(map(int, input().split()))
        graph.append(row)

    start = tuple(map(int, input("Enter the start position (row and column): ").split()))
    end = tuple(map(int, input("Enter the end position (row and column): ").split()))

    path = a_star_algorithm(start, end, graph)

    if path:
        print("Path found:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
