t = int(input())

for case in range(t):

    _ = input()
    lp = input()
    p = ''
    for char in lp:
        if char == 'S':
            p = p + 'E'
        else:
            p = p + 'S'

    print(f"Case #{case + 1}: {p}")