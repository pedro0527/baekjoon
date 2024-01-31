import sys
input = sys.stdin.readline

N, K = map(int, input().split())

Coin = []
for i in range(N):
    Coin.append(int(input()))

Coin.sort(reverse=True)

cnt = 0

for i in Coin:
    if K >= i:
        cnt += K // i
        K %= i

print(cnt)
