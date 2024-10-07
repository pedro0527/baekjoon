cnt = [1, 1, 2, 2, 2, 8]

left = (list(map(int,input().split())))

for i in range(6):
  print(cnt[i]-left[i], end=" ")

