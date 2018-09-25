# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import groupby

def solution(T):
    # write your code in Python 3.6
    half = len(T) // 2
    bucket = groupby(sorted(T))
    i_can_give = 0
    total_candy_types = 0
    for i in bucket:
        total_candy_types += 1
        i_can_give += len(list(i[1])) - 1
    # print(total_candy_types)
    # print(half)
    # print(i_can_give)
    return total_candy_types if i_can_give >= half else (total_candy_types - (half - i_can_give))

A = [3, 4, 7, 7, 6, 6]
# print(solution(A))
A = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]


import time, random
A = [random.randint(0, 1000) for i in range(100000)]
print(solution(A))

# summation = 0
# n = 100
# for i in range(n):
#     S = time.time()
#     solution(A)
#     E = time.time() - S
#     summation += E
#     # tttt.append(E)
# print(summation / n)
