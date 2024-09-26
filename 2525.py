A, B = map(int, input().split())
C = int(input())

sum = B + C
while sum >= 60:
  sum -= 60
  if A == 23:
    A = 0
  else:
    A += 1

print(A, sum)
