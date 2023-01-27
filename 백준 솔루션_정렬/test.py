def most_common (arr):
    no_dup_arr = list(set(arr))
    cnt_Lst = []
    for num in no_dup_arr:
        cnt_Lst.append(arr.count(num))
    print(cnt_Lst)

most_common([1,2,3,3,4,4,4,5])
