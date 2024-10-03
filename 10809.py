S = input()
A_range = 'abcdefghijklmnopqrstuvwxyz'

for i in A_range:
  if i in S:
    print(S.index(i), end = " ")
  else:
    print(-1, end = " ")