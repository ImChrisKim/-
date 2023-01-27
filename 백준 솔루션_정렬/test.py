def most_common (arr):
    count_list = []
    no_dul_arr = list(set(arr))
    no_dul_arr.sort()
    arr.sort()
    print(arr)
    print(no_dul_arr)
    for i in range(len(no_dul_arr)):
        count_list.append(arr.count(no_dul_arr[i]))
    print(count_list)
            
        

most_common([1, 3, 8, -2, 2, 2, 2, 8])