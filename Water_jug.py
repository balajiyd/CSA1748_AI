def water_jug_problem(capacity1, capacity2, target):
    def dfs(jug1, jug2, visited, path):
        print(f"Current state: Jug1 = {jug1}, Jug2 = {jug2}")
        if jug1 == target and jug2 == 0:
            path.append((jug1, jug2))
            print("Target reached!")
            print(f"Final path: {path}")
            return True

        for next_state in get_next_states(jug1, jug2, capacity1, capacity2):
            if next_state not in visited:
                visited.add(next_state)
                path.append(next_state)
                if dfs(next_state[0], next_state[1], visited, path):
                    return True
                path.pop()

        return False

    visited = set()
    path = []
    visited.add((0, 0))
    return dfs(0, 0, visited, path)


def get_next_states(jug1, jug2, capacity1, capacity2):
    next_states = [
        (capacity1, jug2),
        (jug1, capacity2),
        (0, jug2),
        (jug1, 0)
    ]


    pour_amount = min(jug1, capacity2 - jug2)
    next_states.append((jug1 - pour_amount, jug2 + pour_amount))


    pour_amount = min(jug2, capacity1 - jug1)
    next_states.append((jug1 + pour_amount, jug2 - pour_amount))

    return next_states



capacity1 = 4
capacity2 = 3
target = 2

print(water_jug_problem(capacity1, capacity2, target))
