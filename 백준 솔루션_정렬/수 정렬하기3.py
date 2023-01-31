# counting 정렬

# import sys

# N = int(sys.stdin.readline())
# arr = [0] * 10001

# for i in range(N): # [0, 2, 2, 2, 1, 2, 0, 1]
#     arr[int(sys.stdin.readline().rstrip())] += 1

# for j in range(len(arr)):
#     if arr[j] != 0:
#         for count in range(arr[j]):
#             print(j)

# counting 정렬 (함수)

def counting_sort (arr):
    arr_rlt = []
    rlt = [0] * len(arr)
    for i in arr:
        rlt[i] += 1

    for j in range(len(rlt)):
        if rlt[j] != 0:
            for count in range(rlt[j]):
                arr_rlt.append(j)
    return(arr_rlt)

arr = [5, 2, 3, 1, 4, 2, 3, 5, 1, 7]
print(counting_sort(arr))