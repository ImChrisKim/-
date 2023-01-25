# 주어진 수 N개 중에 소수 개수 찾기

N = int(input())

num = list(map(int, input().split()))

Lst = []

def divisor(num):
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
        else:
            continue
    return result


for i in range(N):
    if len(divisor(num[i])) == 2:
        Lst.append(num[i])
    else:
        pass

print(len(Lst))