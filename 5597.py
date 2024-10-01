num = []
p_num = []

for i in range(30):
  num.append(0)

for i in range(28):
  n = int(input())
  num[n-1] = n

for i in range(30):
  if num[i] == 0:
    p_num.append(i+1)

print(min(p_num))
print(max(p_num))
