H, M = map(int, input().split())

if M - 45 < 0 and H == 0:
  H = 23
  M += 15
elif M - 45 < 0:
  M += 15
  H -= 1
else:
  M -= 45

print(H, M)
  