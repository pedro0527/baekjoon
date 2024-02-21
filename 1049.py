import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = []
E = []

for i in range(M):
    A, B = map(int, input().split())
    S.append(A)
    E.append(B)

S = min(S)
E = min(E)

if (S >= E*6):
    print(E*N)

elif(S < E*6):
    if(S < E*(N%6)):
        print(S + S*(N//6))
    else:
        print(S*(N//6) + E*(N%6))
