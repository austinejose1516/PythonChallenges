
def pyramid(rowNo):

    for i in range(rowNo + 1):
        for j in range(i, rowNo):
            print(" ", end='')
        for k in range(1,i*2):
            print("#", end='')
        print("\n")

pyramid(5)