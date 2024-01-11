N = int(input())
i = 1
count = 0

while(i <= N):
    if(i < 10):
        count += 1
    elif(i < 100):
        count += 1
    elif(i < 1000):
        if((i//100 - (i%100)//10) == ((i%100)//10 - i%10)):
            count += 1
    i += 1

print(count) 