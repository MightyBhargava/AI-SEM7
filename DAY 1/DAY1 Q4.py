import itertools
import matplotlib.pyplot as plt


def solve_crypto_arithmetic(puzzle):
    # Extracting unique letters from the puzzle
    letters = set(char for word in puzzle for char in word if char.isalpha())
    letters = list(letters)

    # Generate permutations of digits for the letters
    for perm in itertools.permutations(range(10), len(letters)):
        # Create a mapping of letters to digits
        mapping = dict(zip(letters, perm))

        # Check if the mapping satisfies the puzzle
        if is_solution(puzzle, mapping):
            print("Solution found:")
            for word in puzzle:
                print(f"{translate(word, mapping)}")
            visualize_solution(puzzle, mapping)
            return mapping

    print("No solution found.")
    return None


def is_solution(puzzle, mapping):
    # Evaluate the puzzle with the current mapping
    total = sum(int(translate(word, mapping)) for word in puzzle[:-1])
    result = int(translate(puzzle[-1], mapping))

    # Check if the evaluation matches the result
    return total == result


def translate(word, mapping):
    # Translate a word using the given mapping
    return ''.join(str(mapping[char]) if char.isalpha() else char for char in word)


def visualize_solution(puzzle, mapping):
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot the puzzle equation
    equation = ' + '.join(puzzle[:-1]) + ' = ' + puzzle[-1]
    ax.text(0.5, 0.6, equation, fontsize=14, ha='center', va='center')

    # Plot the solution
    solution = [int(translate(word, mapping)) for word in puzzle]
    ax.text(0.5, 0.4, 'Solution:', fontsize=12, ha='center', va='center')
    ax.text(0.5, 0.3, ', '.join(map(str, solution)), fontsize=12, ha='center', va='center')

    ax.axis('off')
    plt.title('Cryptoarithmetic Problem Solution')
    plt.show()


# Example problem: SEND + MORE = MONEY
puzzle = ["SEND", "MORE", "MONEY"]

# Solve the cryptoarithmetic problem
solve_crypto_arithmetic(puzzle)
