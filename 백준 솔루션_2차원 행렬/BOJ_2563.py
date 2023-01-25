paper_num = int(input())

arr = [[0 for _ in range(100)] for _ in range(100)]

arr_list = []

for i in range(paper_num): # 색종이 붙이는 부분만 1로 치환
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

for i in range(len(arr)): # 2차원 배열 - 1차원으로 변환
    for j in range(len(arr)):
        arr_list.append(arr[i][j])

print(sum(arr_list))

# 도화지 100 x 100 으로 초기화
# 색종이를 10 x 10, 1로 가득한 행렬로 작성
# 색종이의 개수만큼 10 x 10, 1 행렬을 대입
# List의 총합을 더함