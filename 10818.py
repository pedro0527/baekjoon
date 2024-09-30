import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num_list = sorted(num)

print(num_list[0], num_list[N-1])