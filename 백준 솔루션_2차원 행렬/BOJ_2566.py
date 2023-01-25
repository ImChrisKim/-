arr = [[0 for _ in range(9)] for _ in range(9)] # 9X9 행렬 초기화
arr_list = []

for i in range(len(arr)): # 9x9 행렬 입력
    arr[i] = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(len(arr)):
        arr_list.append(arr[i][j])
max_value = max(arr_list)
index_value = arr_list.index(max_value)

print(max_value)
print((index_value // 9) + 1, (index_value % 9) + 1)

# 9X9 행렬을 초기화
# 각 행렬에 값 입력
# 행렬을 1차원으로 변환
# 1차원의 총 합 반환