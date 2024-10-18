board = []

for i in range(5):
  word = list(input())
  board.append(word)

for j in range(15):
  for i in range(5):
    if j < len(board[i]):
      print(board[i][j], end="")