

a = [4, 2, 1, 3]


def reversort(arr):

    cost = 0

    for i in range(len(arr)-1):
        #print('b', arr)
        j = arr.index(min(arr[i:]))
        #print(arr[i:j+1])
        arr[i:j + 1] = arr[i:j + 1][::-1]
        cost += j-i+1
        #print('c', cost)
        #print('a', arr)

    return cost

"""
t = int(input())

for i in range(t):

    n = int(input())
    a = [int(i) for i in input().split()]

    cost = reversort(a)
    print(f"Case #{i + 1}: {cost}")"""