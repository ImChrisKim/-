import sys

def most_common (arr):
    count_list = []
    max_value = []
    no_dul_arr = list(set(arr))
    for i in range(len(no_dul_arr)):
        count_list.append(arr.count(no_dul_arr[i]))
    maximum = count_list.count(max(count_list))
    if maximum == 1:
        return no_dul_arr[count_list.index(maximum)]
    else :    
        for i in range(len(count_list)):
            if count_list[i] == maximum:
                max_value.append(no_dul_arr[i])
        max_value.sort()
        # print(max_value)
        return max_value[1]

N = int(sys.stdin.readline())
arr = []
for count in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print((lambda arr : int(round((sum(arr) / len(arr)), 0)))(arr)) # 평균 구하기
print((lambda arr : arr[(len(arr) // 2)])(arr)) # 중간값 구하기
print(most_common(arr)) #
print((lambda arr : max(arr) - (min(arr)))(arr))
