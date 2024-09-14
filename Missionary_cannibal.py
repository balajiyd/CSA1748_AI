from collections import deque


def is_valid(state):
    m_left, c_left, m_right, c_right = state



    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False
    return True


def get_next_states(state, boat_side):
    m_left, c_left, m_right, c_right = state
    next_states = []


    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for m, c in moves:
        if boat_side == 'left':
            new_state = (m_left - m, c_left - c, m_right + m, c_right + c)
        else:
            new_state = (m_left + m, c_left + c, m_right - m, c_right - c)

        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and \
                0 <= new_state[2] <= 3 and 0 <= new_state[3] <= 3:
            if is_valid(new_state):
                next_states.append(new_state)

    return next_states


def solve_missionary_cannibal(m, c):
    initial_state = (m, c, 0, 0)  # (m_left, c_left, m_right, c_right)
    goal_state = (0, 0, m, c)

    queue = deque([(initial_state, 'left', [])])
    visited = set()
    visited.add((initial_state, 'left'))

    while queue:
        current_state, boat_side, path = queue.popleft()
        path = path + [(current_state, boat_side)]

        m_left, c_left, m_right, c_right = current_state

        print(f"Boat is on the {boat_side} side, State: {current_state}")

        if current_state == goal_state:
            print("\nSolution found:")
            for state, side in path:
                print(f"Boat on {side}, State: {state}")
            return

        next_boat_side = 'right' if boat_side == 'left' else 'left'

        for next_state in get_next_states(current_state, boat_side):
            if (next_state, next_boat_side) not in visited:
                visited.add((next_state, next_boat_side))
                queue.append((next_state, next_boat_side, path))

    print("No solution found.")



solve_missionary_cannibal(3, 3)
