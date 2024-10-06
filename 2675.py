T = int(input())

for i in range(T):
  R, S = map(str, input().split())

  st = []

  for i in S:
    for j in range(int(R)):
      st.append(i)
    
  for i in range(len(st)):
    print(st[i], end="")
  print()
  