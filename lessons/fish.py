# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    survivors = 0
    downstream_que = []
    for i in range(len(A)):
            if B[i] == 1:
               downstream_que.append(A[i])
            elif B[i] == 0 and not downstream_que:
                survivors += 1
            else:
                while downstream_que:
                    if A[i] > downstream_que[-1]:
                        del downstream_que[-1]
                        if not downstream_que:
                            survivors += 1
                    else:
                        break
    survivors += len(downstream_que)
    return survivors

A = [4,3,2,1,5]
B = [0,1,0,0,0]
print(solution(A, B))
A = [4,3,2,1,5]
B = [1,0,1,0,1]
print(solution(A, B))
