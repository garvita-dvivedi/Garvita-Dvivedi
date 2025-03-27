def can_complete_circuit(gas, cost):
    total_gas = 0
    total_cost = 0
    current_gas = 0
    start_index = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]

        if current_gas < 0:
            start_index = i + 1
            current_gas = 0

    if total_gas < total_cost:
        return -1
    return start_index

n = int(input())
gas = list(map(int, input().split()))
m = int(input())
cost = list(map(int, input().split()))

if n != m:
    print(-1)
else:
    result = can_complete_circuit(gas, cost)
    print(result)
