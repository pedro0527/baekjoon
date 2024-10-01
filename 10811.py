N, M = map(int, input().split())

bag = []

for i in range(N):
  bag.append(i+1)


for idx in range(M):
  i, j = list(map(int, input().split()))
  temp = bag[i-1:j]
  temp.reverse()
  bag[i-1:j] = temp

for i in range(N):
  print(bag[i], end=" ")
