N, M = map(int, input().split())
bag = []

for a in range(N):
  bag.append(0)

for a in range(M):
  i,j,k = list(map(int, input().split()))
  for b in range(i-1, j):
    bag[b] = k

for a in range(N):
  print(bag[a], end=" ")

