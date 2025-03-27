def josephus(n, k):
    position = 0
    for i in range(2, n + 1):
        position = (position + k) % i
    return position + 1

n = int(input())
k = int(input())


print(josephus(n, k))
