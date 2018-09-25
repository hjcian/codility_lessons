from functools import reduce
def solution(A):
    # write your code in Python 3.6
    A = sorted(A, reverse=True)
    # posible conbination:
    # + + + - -
    # + + - - -
    # + - - - -
    # - - - - -
    # only comapre (0 1 2) and (0, -1, -2) to find the maximal product
    ret = max(A[0]*A[1]*A[2], A[0]*A[-1]*A[-2])
    return ret

A = [-3,1,2,-2,5,6]
r = solution(A)
print("result: {}".format(r))