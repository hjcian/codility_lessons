# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0 
    minimum = A[0]
    max_profit = 0
    for idx in range(1, len(A)):
        value = A[idx]
        max_profit = max(max(0, value - minimum), max_profit)
        '''
        首先計算目前的淨值(value)與過去買進的最低淨值(minimum)差值是否為正
        若為正或0，與過去取得最佳報酬(max_profit)比較何者為大
        存下歷史最高報酬、紀錄最低淨值
        '''
        minimum = min(minimum, value)
        
    return max_profit
    
        