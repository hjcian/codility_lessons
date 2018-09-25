import numpy as np


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    # 0 <= P < Q < N
    # 只要觀察size 2與3的slices就好，任何更長的slice，其最小值一定在sub-slice裡
    idx = 0
    minimum = (A[0] + A[1]) / 2
    for i in range(N-1):
        cur = (A[i] + A[i + 1]) / 2
        if cur < minimum:
            minimum = cur
            idx = i
        if (i + 2) < N:
            cur = (A[i] + A[i + 1] + A[i + 2]) / 3
            if cur < minimum:
                minimum = cur
                idx = i
    return idx

A = [4,2,2,5,1,5,8]
r = solution(A)
print("result: {}".format(r))