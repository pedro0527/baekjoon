board = []

for i in range(9):
  num = list(map(int, input().split()))
  board.append(num)

max = 0
max_row = 0
max_col = 0

for i in range(9):
  for j in range(9):
    if board[i][j] >= max:
      max = board[i][j]
      max_row = i + 1 
      max_col = j + 1
  

print(max)
print(max_row, max_col, end= " ")