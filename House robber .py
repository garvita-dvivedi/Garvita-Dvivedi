def rob_houses(houses):
    n = len(houses)
    if n == 0:
        return 0
    if n == 1:
        return houses[0]
    if n == 2:
        return max(houses[0], houses[1])
    
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
    
    return dp[-1]

# Input handling
n = int(input())
houses = list(map(int, input().split()))

result = rob_houses(houses)
print(result)
