# counting 정렬

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N): # [0, 2, 2, 2, 1, 2, 0, 1]
    arr[int(sys.stdin.readline().rstrip())] += 1

for j in range(len(arr)):
    if arr[j] != 0:
        for count in range(arr[j]):
            print(j)