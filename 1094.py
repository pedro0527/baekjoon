import sys
input = sys.stdin.readline

X = int(input())
s = 64
cnt = 0

while(X > 0):
    if s > X:
        s = s // 2
    else:
        cnt += 1
        X -= s         
print(cnt)