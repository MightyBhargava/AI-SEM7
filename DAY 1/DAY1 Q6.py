import random
import matplotlib.pyplot as plt


class VacuumCleaner:
    def __init__(self, environment):
        self.environment = environment  # 2x2 grid representing rooms (0: clean, 1: dirty)
        self.position = (0, 0)  # Starting position of the vacuum cleaner

    def sense(self):
        return self.environment[self.position[0]][self.position[1]]

    def clean(self):
        self.environment[self.position[0]][self.position[1]] = 0
        print(f"Room ({self.position[0]}, {self.position[1]}) cleaned.")

    def move(self):
        # Randomly choose a direction (0: up, 1: down, 2: left, 3: right)
        direction = random.randint(0, 3)

        if direction == 0 and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == 1 and self.position[0] < 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 2 and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 3 and self.position[1] < 1:
            self.position = (self.position[0], self.position[1] + 1)

        print(f"Moved to room ({self.position[0]}, {self.position[1]}).")

    def run(self):
        print("Starting the Vacuum Cleaner simulation...")

        # Create figure and axis for plotting
        fig, ax = plt.subplots()

        # Plot initial environment
        self.plot_environment(ax)

        while any(any(row) for row in self.environment):
            if self.sense() == 1:
                self.clean()
                # Clear previous plot and re-plot updated environment
                ax.clear()
                self.plot_environment(ax)
                plt.pause(1)  # Pause to visualize cleaning action

            self.move()
            # Clear previous plot and re-plot updated environment
            ax.clear()
            self.plot_environment(ax)
            plt.pause(1)  # Pause to visualize movement action

        print("All rooms cleaned. Simulation complete.")

    def plot_environment(self, ax):
        # Define colors for clean (white) and dirty (gray) rooms
        colors = ['white', 'gray']

        # Plot each room in the environment
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f'({j}, {i})', ha='center', va='center')
                ax.fill_between([j, j + 1], [i, i], [i + 1, i + 1], color=colors[self.environment[i][j]])

        ax.set_xlim(0, 2)
        ax.set_ylim(0, 2)
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Vacuum Cleaner Simulation')
        plt.pause(0.1)  # Pause to update plot


# Create a 2x2 grid environment (0: clean, 1: dirty)
environment = [
    [1, 0],
    [1, 1]
]

# Create and run the Vacuum Cleaner simulation
vacuum = VacuumCleaner(environment)
vacuum.run()
