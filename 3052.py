num = []
cnt = 10

for i in range(10):
  n = int(input())
  num.append(n%42)
  
for i in range(10):
  for j in range(i, 9):
    if num[i] == num[j+1]:
      cnt -= 1
      break

print(cnt)
