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
