import itertools


def calculate_distance(matrix, route):
    distance = 0
    for i in range(len(route) - 1):
        distance += matrix[route[i]][route[i + 1]]
    distance += matrix[route[-1]][route[0]]  # Return to the starting city
    return distance


def travelling_salesman(matrix):
    cities = list(range(len(matrix)))
    shortest_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        current_distance = calculate_distance(matrix, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = perm

    return shortest_route, min_distance


def main():
    # Get number of cities from the user
    num_cities = int(input("Enter the number of cities: "))

    # Initialize the distance matrix
    matrix = []
    print("Enter the distance matrix row by row:")
    for i in range(num_cities):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Solve TSP
    route, distance = travelling_salesman(matrix)

    # Output the result
    print(f"The shortest route is: {route} with a distance of {distance}")


if __name__ == "__main__":
    main()
