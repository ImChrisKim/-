def prime(n): # n 이하의 소수

    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    primes = []
    
    for i in range(2, int(n**0.5)+1):
        if arr[i] == True:
            for j in range(i*2, n+1, i):
                arr[j] = False
    
    for i in range(n):
        if arr[i] == True:
            primes.append(i)
    return primes

def divisor (n): # 약수 리스트
    divisor_arr = []
    for i in range (1, n+1):
        if n % i == 0 :
            divisor_arr.append(i)
    return divisor_arr

def isPrime(n): # 소수인지 확인하는 함수
    divisor_arr = [] # 약수 리스트
    for i in range (1,n+1):
        if n % i == 0:
            divisor_arr.append(i)
    if len(divisor_arr) == 2:
        return n
    else:
        return False

