x1 = 4523
v1 = 8092
x2 = 9419
v2 = 8076

def kangaroo(x1, v1, x2, v2):

    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            print("YES")
        x1+=v1
        x2+=v2
    ("NO")

kangaroo(x1, v1, x2, v2)
