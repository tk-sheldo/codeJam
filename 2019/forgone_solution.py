

def split(n):

    n = list(str(n))

    other = 0
    p = 1

    while p <= len(n):

        #print(n[-p])

        if n[-p] == '4':

            other += 10**(p-1)

            n[-p] = '3'

        p += 1

    return (int(''.join(list(n))), other)


t = int(input())

for i in range(t):
    n = int(input())
    a, b = split(n)
    print(f"Case #{i+1}: {a} {b}")




