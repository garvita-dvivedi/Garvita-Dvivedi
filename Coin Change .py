def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Input handling
n = int(input())
coins = list(map(int, input().split()))
amount = int(input())

result = coin_change(coins, amount)
print(result)
