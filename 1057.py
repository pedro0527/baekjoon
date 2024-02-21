import sys
input = sys.stdin.readline

N, num1, num2 = map(int, input().split())

cnt = 0

while num1 != num2:
    num1 -= num1 // 2
    num2 -= num2 // 2
    cnt += 1
print(cnt)

