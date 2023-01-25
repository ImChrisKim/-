# M과 N사이의 소수 출력

m, n = map(int, input().split())

Lst = list(range(n+1)) # 0 ~ n 까지의 리스트 선언
Lst[0] = False
Lst[1] = False
prime = []

for i in range(2, n+1): # 2의 배수부터 False로 반환
    prime.append(Lst[i])
    for j in range(i*2, n+1, i):
        Lst[j] = False

for i in range(len(prime)): # 출력
    if prime[i] != False:
        if prime[i] >= m:
            print(prime[i])