import sys

N = int(input())
n_score = []

score = list(map(int, sys.stdin.readline().split()))

for i in range(N):
  n_score.append(score[i]/max(score))

print(sum(n_score) / N * 100)