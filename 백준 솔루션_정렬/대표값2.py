arr = []

for i in range(5):
    num = int(input())
    arr.append(num)
    

print(int(sum(arr) / len(arr)))
arr.sort()
print(arr[2])