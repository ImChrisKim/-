N, M = list(map(int, input().split())) # N, M값 입력

arr_1 = [[0 for _ in range(M)] for _ in range(N)] # N x M 배열 0으로 초기화
arr_2 = [[0 for _ in range(M)] for _ in range(N)]

for i in range(len(arr_1)): # N x M 배열 입력1
    arr_1[i] = list(map(int, input().split()))

for i in range(len(arr_2)): # N x M 배열 입력2
    arr_2[i] = list(map(int, input().split()))

for i in range(len(arr_1)): # N x M 행렬 2개 덧셈
    arr_sum = 0
    for j in range(len(arr_2[0])):
        arr_sum = arr_1[i][j] + arr_2[i][j]
        print(arr_sum, end = ' ')
    print("")
    
    # M, N 값을 입력하여 M x N 2차원 배열(행렬) 2개 입력
    # 2개의 2차원 배열을 더하는 반복문을 작성 
    # 반복문 작성시 행 x 열의 길이가 각각 다름에 따라 범위 설정 조심
