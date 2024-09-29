total = int(input())
var = int(input())
total_price = 0

for i in range(var):
  price, cnt = map(int, input().split())
  total_price += price * cnt

if total == total_price:
  print("Yes")
else:
  print("No")
