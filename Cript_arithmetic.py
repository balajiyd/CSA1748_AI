from itertools import permutations


def send_more_money():
    # The unique letters in the puzzle
    letters = 'SENDMORY'


    for perm in permutations(range(10), 8):

        s, e, n, d, m, o, r, y = perm


        send = 1000 * s + 100 * e + 10 * n + d
        more = 1000 * m + 100 * o + 10 * r + e
        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y


        if send + more == money:
            print(f"S = {s}, E = {e}, N = {n}, D = {d}, M = {m}, O = {o}, R = {r}, Y = {y}")
            return


# Call the function
send_more_money()
