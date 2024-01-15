N = int(input())
get_num = set(list(map(int, input().split())))

M = int(input())
find_num = list(map(int, input().split()))

for i in range(M):
    if find_num[i] in get_num:
        print(1, end = " ") 
    else:
        print(0, end = " ")


# for num in find_num :
#     if num in get_num:
#         print(1, end = " ") 
#     else:
#         print(0, end = " ")