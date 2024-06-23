import networkx as nx
import matplotlib.pyplot as plt


class MapColoringProblem:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.solution = {}

    def is_valid(self, node, color, assignment):
        for neighbor in self.graph[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.graph):
            return assignment

        node = self.select_unassigned_variable(assignment)
        for color in self.colors:
            if self.is_valid(node, color, assignment):
                assignment[node] = color
                result = self.backtracking_search(assignment)
                if result:
                    return result
                assignment.pop(node)
        return None

    def select_unassigned_variable(self, assignment):
        for node in self.graph:
            if node not in assignment:
                return node
        return None

    def solve(self):
        solution = self.backtracking_search()
        if solution:
            self.solution = solution
            return True
        else:
            return False

    def get_solution(self):
        return self.solution


def draw_map(graph, solution):
    G = nx.Graph()
    for node in graph:
        G.add_node(node)
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)  # Positions for all nodes

    if solution:
        node_colors = [solution[node] for node in G.nodes]
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000, font_size=12, font_weight='bold',
                cmap=plt.cm.tab10)
        plt.title("Map Coloring Solution", fontsize=15)
    else:
        plt.figure(figsize=(8, 6))
        nx.draw(G, pos, with_labels=True, node_size=1000, font_size=12, font_weight='bold')
        plt.title("No Solution Found", fontsize=15)

    plt.show()


def main():
    # Example graph representing regions and their neighbors
    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW']
    }

    # Example colors available
    colors = ['red', 'green', 'blue']

    map_coloring_problem = MapColoringProblem(graph, colors)
    if map_coloring_problem.solve():
        solution = map_coloring_problem.get_solution()
        print("Solution found:")
        for node, color in solution.items():
            print(f"{node}: {color}")
    else:
        print("No solution found.")

    draw_map(graph, solution)


if __name__ == "__main__":
    main()
