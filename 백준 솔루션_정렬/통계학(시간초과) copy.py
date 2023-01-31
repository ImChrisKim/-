import sys

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

def most_common (arr):
    no_dup_arr = list(set(arr))
    cnt_Lst = []
    counting_sort(no_dup_arr)
    for num in no_dup_arr:
        cnt_Lst.append(arr.count(num))
    max_count = max(cnt_Lst) # 최빈값
    if cnt_Lst.count(max_count) == 1:
        return no_dup_arr[cnt_Lst.index(max_count)]
    else :
        for i in range(len(cnt_Lst)):
            if cnt_Lst[i] == max_count:
                return no_dup_arr[i]

N = int(sys.stdin.readline())
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())
counting_sort(arr)
print((lambda arr : int(round((sum(arr) / len(arr)), 0)))(arr)) # 평균 구하기
print((lambda arr : arr[(len(arr) // 2)])(arr)) # 중간값 구하기
print(most_common(arr)) #
print((lambda arr : max(arr) - (min(arr)))(arr))
