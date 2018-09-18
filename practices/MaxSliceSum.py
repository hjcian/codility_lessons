# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(A):
    # write your code in Python 3.6
    # negitive_vec = [i for i in range(len(A)) if A[i] < 0]
    # if len(negitive_vec) == len(A):
    #     return min(A)
    
    # negitive_vec.insert(0, -1)
    # negitive_vec.insert(len(negitive_vec), len(A))
    # # print(negitive_vec)
    # max_sum = 0
    # for idx in range(len(negitive_vec) - 1):
    #     left = negitive_vec[idx] + 1
    #     right = negitive_vec[idx + 1]
    #     # print(left, right)
    #     if right >= left:
    #         max_sum = max(max_sum, sum(A[left:right]))
    # # print(max_sum)
    # return max_sum

    # max_idx = 0
    # maximum = A[max_idx]
    # for i in range(1, len(A)):
    #     if A[i] > maximum:
    #         maximum = A[i]
    #         max_idx = i
    # max_left = max_right = A[max_idx]
    # for i in range(max_idx + 1, len(A)):
    #     max_right = max(max_right + A[i], max_right)
    # for i in range(max_idx - 1, 0, -1):
    #     max_left = max(max_left + A[i], max_left)

    # return max_left + max_right - A[max_idx]

    # write your code in Python 3.6
    # hint: https://rafal.io/posts/codility-max-slice-sum.html
    current_max = A[0]
    maxi = A[0]
    for i in A[1:]:
        # print("i: {} acc: {} ".format(i, current_max))
        current_max = max(i, current_max + i)
        # 此步在計算目前的值(i)，與連加到目前的值(current_max + i)為止，誰比較大
        # 連加值有正有負，若能一直保持在連加起來最大的狀態，一定比某個單一值還大
        # 故若某一單值比連加的值還大，表示前面的數組連加起來的值都該被淘汰，由現在的
        # 值開始連加
        # print("max of i: {} sum: {}".format(i, current_max))
        maxi = max(maxi, current_max)
        # 每一次連加的值都與歷史連加值相比，保持最大的連加值
    return maxi
        
    
A = [3,2,-6,4,0]
print(solution(A))

for i in range(len(A), len(A)):
    print(i)