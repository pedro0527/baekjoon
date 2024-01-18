Px1, Py1, Px2, Py2 = map(int, input().split()) 
Qx1, Qy1, Qx2, Qy2 = map(int, input().split())

if(Px2 < Qx1 or Py2 < Qy1 or Qx2 < Px1 or Qy2 < Py1):
    print("NULL")
elif((Px2 == Qx1 and Py2 == Qy1) or (Px1 == Qx2 and Py2 == Qy1) or 
     (Px1 == Qx2 and Py1 == Qy2) or (Px2 == Qx1 and Py1 == Qy2)):
    print("POINT")
elif(Px1 == Qx2 or Px2 == Qx1 or Py1 == Qy2 or Py2 == Qy1):
    print("LINE")
else:
    print("FACE")

# 1. 제일 먼저 NULL의 case를 분류함 
# 2. POINT는 4곳에서만 일어나므로 POINT의 경우 분류함
# 3. elif이므로 POINT의 case는 제외되어 있으므로 
#    점중에서 X값이나 Y값만 같아도 LINE이 일어난다.
# 4. 마지막으로 else를 이용하여 FACE의 경우를 나눠준다.