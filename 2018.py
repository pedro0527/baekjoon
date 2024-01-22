N = int(input())

sum = 0
cnt = 0
first = 0
last = 0

while(last <= N):
    if(sum < N):
        last += 1
        sum += last
    elif(sum > N):
        sum -= first
        first += 1
    else:
        cnt += 1
        last += 1
        sum += last
        
print(cnt)