# M과 N 사이 소수의 개수

M = int(input)
N = int(input)

if M > N: # 항상 N값이 M값보다 더 크게 유지

    M, N = N, M

else :
    pass

num_range = list(range(M,N+1))

Lst = []

def divisor(num): # 약수 구하는 함수
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
        else:
            continue
    return result


for i in range(0,N-M+1): # List중 약수가 2개인 것을 추출
    if len(divisor(num_range[i])) == 2:
        Lst.append(num_range[i])
    else:
        continue

if len(Lst) == 0:
    print(-1)
else :
    print(sum(Lst))
    print(min(Lst))