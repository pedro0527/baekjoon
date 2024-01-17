C = int(input())
i = 0

for i in range (C):

    Score = list(map(int, input().split()))
    Count = 0
    
    for j in Score[1:]:
        Average = sum(Score[1:]) / Score[0]
    
        if(j > Average):
            Count += 1

    Percent = Count/Score[0]*100

    print('%.3f' % Percent + '%')