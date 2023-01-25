num = int(input())

if num % 2 == 1:

    pass

else :
    N = num // 2
    arr = [True] * (N+1) # N 보다 작은 소수
    arr[0] = False
    arr[1] = False
    primes = []

    for i in range(2, int(N**0.5)+1):
        if arr[i] == True:
            for j in range(i*2, N+1, i):
                arr[j] = False

    for i in range(N):
        if arr[i] == True:
            primes.append(i)

    arr_B = []
    for i in range(len(primes)):
        for j in range(len(primes)):
            if primes[i] + primes[j] == num:
                arr_B.append(primes[i])
    a = len(arr_B)
    if a % 2 == 1:
        print(f"{arr_B[a//2]} {arr_B[a//2]}")
    if a % 2 == 0:
        print(f"{arr_B[(a//2) - 1]} {arr_B[a//2]}")
                
