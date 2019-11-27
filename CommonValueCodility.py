'''

Task You are given an implementation of a function:

That given a non-empty array A of N non-negative integers and a non-empty array B of M non-negative integers, returns the minimal value that occurs in both arrays. If there is no such value, the function should return -1.

For example, given arrays A and B such that
A [0] = 1 B [0] = 4 A [1] = 3 B [1] = 2 A[2] =2 B[2] = 5 A [3] = 1 B [3] = 3 B[4] = 2 your function should return 2, since 2 is the minimal value which occurs in both arrays A and B (another value which occurs in both arrays is 3).

The goal of the exercise is to find and fix the bug(s) in the implementation. You can modify at most two lines.
Write an efficient algorithm for the following assumptions.

'''

# Solution

A = [2, 3, 4]
B = [1, 2, 1]

P = [1, 3, 2, 1]
Q = [4, 3, 5, 3, 2]

R = [2, 1]
S = [3, 3]

def solution(A, B):

    A.sort()
    B.sort()
    i = 0

    for a in A:
        while i < len(B) - 1 and B[i] < a: # --- Change if to while and your answer is correct ---
            i += 1
            if a == B[i]:
                print(a)
    if not a:
        print(-1)

solution(A, B)
