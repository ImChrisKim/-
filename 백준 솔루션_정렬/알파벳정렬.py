N = int(input())

tem_str = [0] * N
arr_len = [0] * N
arr = [0] * N

for i in range(N): # 알파벳 array값 받기
    tem_str[i] = input()

arr_str = list(set(tem_str)) # 중복값 제거

for i in range(len(arr_str)):
    arr_len = len(arr_str[i])
    arr[i] = (arr_len[i], arr_str[i])

print(arr)