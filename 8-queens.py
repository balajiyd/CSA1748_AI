import itertools

def solve_queens(n):
    def is_safe(board):
        for i in range(n):
            for j in range(i+1, n):
                if abs(board[i] - board[j]) == abs(i - j):
                    return False
        return True

    result = []
    for board in itertools.permutations(range(n)):
        if is_safe(board):
            result.append(["."*i + "Q" + "."*(n-i-1) for i in board])
    return result

n = 8
solutions = solve_queens(n)
for i, solution in enumerate(solutions):
    print("Solution", i+1)
    for row in solution:
        print(row)
    print()
