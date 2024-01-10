N = int(input())

x = 5
y = 3
count = 0

for i in range(2000):
    for j in range(2000):
        if(N - ((x*i) + (y*j)) == 0):
            a = i
            b = j
            count += 1
            break     
            

if(count == 0):
    print(-1)
else:
    print(a + b)