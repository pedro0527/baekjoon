n = int(input())
i = 1
sum = 0

while i <= n:
  sum += i
  i += 1

print(sum)

# 2번째 방법
# n = int(input())
# print(sum(range(1, n+1)))로도 풀 수 있다. 

#3번째 방법
# sum = n*(n+1) // 2 -> 등차수열 공식으로도 풀 수 있다.