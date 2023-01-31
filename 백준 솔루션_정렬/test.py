def most_frequent(List):
    counter = 0
    arr = set()
    
    for i in List: # i : [2, 1, 2, 2, 1, 1, 3]
        max_frequency = List.count(i) # curr_frequency : 3
        if(max_frequency >= counter): # if 3 > 0
            counter = max_frequency # counter : 3
            arr.add(i) # num : 2
 
    rlt = list(arr)
    if len(rlt) == 1:
        return rlt
    else :
        return rlt

List = [-1, -2, -3, -1, -2]
print(most_frequent(List))