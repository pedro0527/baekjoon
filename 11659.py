import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Num = list(map(int,input().split()))

Sum = [0]
hap = 0

for i in range(N):
    hap += Num[i] 
    Sum.append(hap)

for k in range(M):
    i, j = map(int, input().split())
    print(Sum[j] - Sum[i-1])
    