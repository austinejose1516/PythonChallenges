a = [1, 3, 5, 7, 9]

def maxminsum(arr):

    total = 0
    for i in range(len(arr)):
        total += arr[i]
    print(total-max(arr), total - min(arr))

maxminsum(a)
