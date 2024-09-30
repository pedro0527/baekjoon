N = 9
num = []

for i in range(N):
  num.append(int(input()))

print(max(num))
print(num.index(max(num)) + 1)
