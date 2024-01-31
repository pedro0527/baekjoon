import sys
input = sys.stdin.readline

N = int(input())
len = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]
total = 0

for i in range(N-1):
    if min > price[i]:
        min = price[i]
    
    total += min * len[i]

print(total)