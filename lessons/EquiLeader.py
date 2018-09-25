# -*- coding: utf-8 -*-
from itertools import groupby

def solution(A):
    # groupby: http://ot-note.logdown.com/posts/1379449
    # 神奇的功能
    # solution reference
    # https://blog.csdn.net/LookEsat/article/details/44752923
    # http://cain19811028.blogspot.com/2017/02/pythoncodility-in-python-lesson-8_23.html
    key = value = -1
    maxGroup = max(groupby(sorted(A)), key = lambda x: len(list(x[1])))
    key = maxGroup[0]
    value = len(list(filter(lambda x: x == key, A)))
    if value <= len(A) / 2:
        return 0
    '''
    理由是如果至少有一個index分成兩邊，且剛好有一個數字在兩邊都是dominator
    表示此值出現的次數一定要超過len(A) / 2，這樣切成兩段時才能在兩邊同時占優
    接著，equi-leader出現時，一定也是此key同時在兩邊占優
    此問題就是在問，此占優的key，切分N-1次後，出現幾次同時兩邊占優
    '''
    N = len(A)
    equi_cnt = 0
    left = 0
    right = value
    for idx, num in enumerate(A):
        if num == key:
            left += 1
            right -= 1
        left_len = idx + 1
        right_len = N - left_len
        if left > left_len / 2 and right > right_len / 2:
            equi_cnt += 1
    '''
    初始化左半邊的key數量為left；右半邊的key數量為right
    此時從index=0開始走訪一次所有的元素，如果此時的num為key，
    則左半邊的數量++、右半邊的數量--
    然後檢查左半邊的數量是否占優；右半邊的數量是否占優
    皆占優則總計數++
    '''
    return equi_cnt


A = [4,3,4,4,4,2]
print(solution(A))