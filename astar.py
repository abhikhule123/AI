from queue import PriorityQueue

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the movements: left, right, up, down
movements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def heuristic(state):
    # Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_row = (value - 1) // 3
                target_col = (value - 1) % 3
                distance += abs(i - target_row) + abs(j - target_col)
    return distance

def get_blank_position(state):
    # Find the position of the blank tile (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state, blank_row, blank_col):
    # Generate the neighboring states
    neighbors = []
    for move in movements:
        new_row = blank_row + move[0]
        new_col = blank_col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            neighbor = [row[:] for row in state]
            neighbor[blank_row][blank_col], neighbor[new_row][new_col] = neighbor[new_row][new_col], neighbor[blank_row][blank_col]
            neighbors.append(neighbor)
    return neighbors

def solve_puzzle(initial_state):
    # Initialize the priority queue
    pq = PriorityQueue()
    pq.put((0, initial_state))

    # Initialize the visited set
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    # Initialize the parent dictionary
    parent = {}
    parent[tuple(map(tuple, initial_state))] = None

    while not pq.empty():
        # Get the state with the minimum cost
        cost, current_state = pq.get()

        # Check if the current state is the goal state
        if current_state == goal_state:
            # Reconstruct the path
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parent[tuple(map(tuple, current_state))]
            path.reverse()
            return path

        # Find the position of the blank tile
        blank_row, blank_col = get_blank_position(current_state)

        # Generate the neighboring states
        neighbors = get_neighbors(current_state, blank_row, blank_col)

        for neighbor in neighbors:
            # Check if the neighbor has been visited
            if tuple(map(tuple, neighbor)) not in visited:
                # Calculate the cost of the neighbor
                neighbor_cost = cost + 1 + heuristic(neighbor)

                # Add the neighbor to the priority queue
                pq.put((neighbor_cost, neighbor))

                # Add the neighbor to the visited set
                visited.add(tuple(map(tuple, neighbor)))

                # Set the parent of the neighbor
                parent[tuple(map(tuple, neighbor))] = current_state

    # No solution found
    return None

# Define the initial state
initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Solve the puzzle
solution = solve_puzzle(initial_state)

# Print the solution
if solution is not None:
    for step, state in enumerate(solution):
        print("Step:", step)
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
