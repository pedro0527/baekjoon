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


# 1~30까지를 배열에 저장하고 입력값 28개를 
# remove를 사용해서 제거해줄 수 있다.
# student=[i for i in range(1,31)]
# for i in range(28):
#     data=int(input())
#     student.remove(data)
# print(min(student))
# print(max(student))