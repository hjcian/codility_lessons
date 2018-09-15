def solution(A):
    # write your code in Python 3.6
    # N = len(A)
    # maximum = A[0] + A[0] + (0 - 0)
    # for i in range(N):
    #     for j in range(N):
    #         maximum = max(A[i] + A[j] + (i - j), maximum)
    # return maximum
    # think divide and conquer
    # max. vlaue of first row is 
    N = len(A)
    maxJ = 0
    maximum = A[0]
    for j in range(N):
        if  A[j] - j > maximum:
            maximum = A[j] - j
            maxJ = j
    maxI = 0
    
    maximum = A[0]
    for i in range(N):
        if  A[i] + i > maximum:
            maximum = A[i] + i
            maxI = i
    print(maxI, maxJ)
    ret = A[maxI] + maxI + A[maxJ] - maxJ
    
    return ret


A = [1, 3, -3]
r = solution(A)
print(r)
A = [-8, 4, 0, 5, -3, 6]
r = solution(A)
print(r)
