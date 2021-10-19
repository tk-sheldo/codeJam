

def GCF(a, b):
    if a < b:
        temp = b
        b = a
        a = temp

    r = a%b

    if r == 0:
        return b
    else:
        return GCF(b, r)

t = int(input())

for case in range(t):

    n, l = list(map(int, input().split(' ')))

    code = list(map(int, input().split(' ')))

    primes = ['X']
    primes.append(GCF(code[0], code[1]))

    primes[0] = code[0]/primes[1]

    for i in range(len(code)-1):
        primes.append(code[i+1]/primes[i+1])

    primes = list(map(int, primes))

    l = list(dict.fromkeys(primes))
    l.sort()
    #print(l)

    d = {}
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(len(l)):
        d[l[i]] = letters[i]

    #print(d)

    broken = ''

    for num in primes:
        broken = broken + d[num]


    print(f"Case #{case + 1}: {broken}")

