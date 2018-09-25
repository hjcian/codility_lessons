def solution(A):
    # write your code in Python 3.6
    A = sorted(A, reverse=True)
    for i in range(len(A) - 2):
        if A[i + 1] + A[i + 2] > A[i]:
            return 1
    return 0
A = [10,2,5,1,8,20]
r = solution(A)
print("result: {}".format(r))