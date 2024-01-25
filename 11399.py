N = int(input())
P = list(map(int, input().split()))

P.sort()

Sum = []
Min = 0

for i in range(N):
    Sum.append(P[i])
    Min += sum(Sum)

print(Min)
