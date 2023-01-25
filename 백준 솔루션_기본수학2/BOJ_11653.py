# N 을 소인수분해 하는 문제

def divisor (num) :
    divisor_arr = [] # 약수 리스트
    for i in range (1,num+1):
        if num % i == 0:
            divisor_arr.append(i)
        else :
            continue
    return divisor_arr

def prime (arr) : # 약수 리스트 중 소수 추출
    prime_arr = []
    for i in range(len(arr)):
        if len(divisor(arr[i])) == 2:
            prime_arr.append(arr[i])
        else :
            continue
    return prime_arr

N = int(input())
prime_Lst = prime(divisor(N))
divisor_Lst = divisor(N)


for i in range(len(prime_Lst)):
    while True :
        if N % prime_Lst[i] == 0:
            print(prime_Lst[i])
            N /= prime_Lst[i]
        else :
            break