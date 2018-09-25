def solution(A):
    # write your code in Python 3.6
    max_occurs = 0
    dominator_idx = 0
    count = {}
    for idx, num in enumerate(A):
        data = count.get(num, 0)
        data += 1
        count.update({num: data})
        if data > max_occurs:
            max_occurs = data
            dominator_idx = idx
    # print(count)
    # print(max_occurs, dominator, dominator_idx)
    return dominator_idx if max_occurs > len(A)/2 else -1

A = [3, 4, 3, 2, 3, -1, 3, 3] 
print(solution(A))