t = int(input())

for _ in range(t):

    a, b = [int(i) + 1 for i in input().split()]
    _ = int(input())

    got_it = False

    while not got_it:

        midpoint = ((b - a) // 2) + a
        print(midpoint, flush=True)

        response = input()

        if response == "CORRECT":
            got_it = True
        elif response == "TOO_BIG":
            b = midpoint
        elif response == "TOO_SMALL":
            a = midpoint





