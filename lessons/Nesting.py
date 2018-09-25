# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def isLeft(c):
    return c in ('(',) if c else 0

def isRight(c):
    return c in (')',) if c else 0

def isPair(left, right):
    return (left, right) in (("(", ")"),)

def solution(S):
    # write your code in Python 3.6
    if not S:
        return 1
    queue = []
    for c in S:
        if isRight(c):
            if queue and isLeft(queue[-1]) and isPair(queue[-1], c):
                del queue[-1]
            else:
                return 0
        else:
            queue.append(c)
    if not queue:
        return 1
    else:
        return 0


S = "(()(())())"
print(solution(S)) # 1
S = "())"
print(solution(S)) # 0