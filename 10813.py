N, M = map(int, input().split())
box = []

for idx in range(1, N+1):
  box.append(idx)

for idx in range(M):
  i, j = list(map(int, input().split()))
  temp = 0

  temp = box[i-1]
  box[i-1] = box[j-1]
  box[j-1]=temp

for idx in range(N):
  print(box[idx], end=" ")