A, B = input().split()

num1 = int(A[2]+A[1]+A[0])
num2 = int(B[2]+B[1]+B[0])

if num1 > num2:
  print(num1)
else:
  print(num2)

# [::-1]를 사용하면 역순으로 슬라이싱을 할 수 있다.
# [시작인덱스:종료인덱스:step]

