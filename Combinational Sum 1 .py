def find_combinations(arr, target, start, path, result):
    if target == 0:
        result.append(path)
        return
    if target < 0:
        return
    
    for i in range(start, len(arr)):
        find_combinations(arr, target - arr[i], i, path + [arr[i]], result)

def combination_sum(arr, target):
    arr.sort()
    result = []
    find_combinations(arr, target, 0, [], result)
    return result

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

result = combination_sum(arr, target)

if not result:
    print("Empty")
else:
    for combination in result:
        print(" ".join(map(str, combination)))
