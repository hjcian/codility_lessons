# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    forward = [0] * N
    for idx in range(1, N - 1):
        forward[idx] = max(0, forward[idx - 1] + A[idx])
    backward = [0] * N
    for idx in range(N - 2, 0, -1):
        backward[idx] = max(0, backward[idx + 1] + A[idx])
    # print(forward)
    # print(backward)
    max_double_slice = 0
    for idx in range(1, N - 1):
        max_double_slice = max(max_double_slice, forward[idx - 1] + backward[idx + 1])
    # print(max_double_slice)
    return max_double_slice
    
        



A = [3, 2, 6, -1, 4, 5, -1, 2]
solution(A)

