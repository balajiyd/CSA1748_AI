from collections import deque


def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()

def is_goal(state, goal):
    return state == goal

def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j

def swap(state, i1, j1, i2, j2):
    new_state = [row[:] for row in state]
    new_state[i1][j1], new_state[i2][j2] = new_state[i2][j2], new_state[i1][j1]
    return new_state

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if 0 <= nx < 3 and 0 <= ny < 3:
            neighbors.append(swap(state, x, y, nx, ny))
    return neighbors

# BFS to solve the 8-puzzle
def solve_8_puzzle(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, 0)])  # (current_state, moves_taken)
    visited.add(tuple(map(tuple, initial_state)))

    while queue:
        current_state, moves_taken = queue.popleft()

        if is_goal(current_state, goal_state):
            return current_state, moves_taken

        for neighbor in get_neighbors(current_state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                queue.append((neighbor, moves_taken + 1))

    return None, -1


initial_state = [
    [1, 2, 3],
    [4, 5, 0], 
    [6, 7, 8]
]


goal_state = [
    [1, 2, 3],
    [4, 0, 5],  
    [6, 7, 8]
]

final_state, moves_taken = solve_8_puzzle(initial_state, goal_state)

if final_state:
    print("Final state reached:")
    print_puzzle(final_state)
    print(f"Number of moves taken: {moves_taken+1}")
else:
    print("No solution found!")
