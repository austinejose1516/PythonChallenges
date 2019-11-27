'''

Write a function:

def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

'''

# Solution

a = [1, 2, 3, 4]


def missint(a):
    cleana = sorted(set(a))
    a_max = max(cleana)

    lst = []

    for i in cleana:

        if i < 0:
            return (1)

    for i in range(1, a_max + 1):

        if i in cleana:
            continue
        else:
            lst.append(i)

    if not lst:
        print(a_max + 1)
    else:
        print(min(lst))

missint(a)