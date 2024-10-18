board = []
cnt = 0

board = [[0 for i in range(100)] for j in range(100)] 

num = int(input())

for i in range(num):
  width, height = map(int, input().split())
  for j in range(width, width+10, 1):
    for k in range(height, height+10, 1):
      board[j][k] = 1

for i in range(100):
  for j in range(100):
    if board[i][j] == 1:
      cnt += 1

print(cnt)