N, K = map(int, input().split())

arr = list(map(int, input().split())) # [100, 76, 85, 93, 98]

arr.sort()

print(arr[-K])

