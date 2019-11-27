
def staircase(n):

    for i in range(1, n+1):
        for j in range(i, n):
            print(' ', end = '')
        for l in range(i):
            print('#', end = '')
        print('\n')

staircase(5)