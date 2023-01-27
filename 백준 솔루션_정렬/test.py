def most_common (arr):
    count_list = []
    max_value = []
    no_dul_arr = list(set(arr))
    no_dul_arr.sort()
    arr.sort()
    for i in range(len(no_dul_arr)):
        count_list.append(arr.count(no_dul_arr[i]))
    for i in range(len(count_list)):
        if count_list[i] == max(count_list):
            max_value.append(no_dul_arr[i])
    if len(max_value) == 1:
        return max_value[:]
    else :
        max_value.sort()
        return max_value[-2]
