N, X = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in range(N):
  if A[i] < X:
    print(A[i], end=" ")