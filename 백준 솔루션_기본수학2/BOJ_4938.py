# n 보다 크고 2n 보다 작은 소수는 반드시 존재한다 - 베르트랑 공준

while True :

    n = int(input())

    if n == 0:
        break

    else :
        Lst = [True] * (2*n+1) # 0 ~ 2n 까지의 True 리스트 선언
        Lst[0] = False
        Lst[1] = False
        prime = []

        for i in range(2, 2*n+1): # 2의 배수부터 False로 반환
            if Lst[i] == True:
                for j in range(i*2, 2*n+1, i):
                    Lst[j] = False

        for i in range(n+1, 2*n+1):
            if Lst[i] == True:
                prime.append(i)

        print(len(prime))
        
# 소수를 구하는 최단 알고리즘 활용
# 0 ~ 2n 까지의 True 리스트를 선언
# 2의배수부터 3의배수, 4의배수 순으로 False로 전환
# 최종 True인 값의 Index만 반환