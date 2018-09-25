# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import re

def solution(T, R):
    # write your code in Python 3.6
    d = {}
    for idx in range(len(T)):
        test_name = T[idx]
        m = re.search("(\d)", test_name)
        g = m.group(0)
        data = d.get(g, None)
        if R[idx] != "OK":
            d.update({g: False})
        elif R[idx] == "OK" and data == None:
            d.update({g: True})
    # print(d)
    pass_cnt = sum([1 if d[g] else 0 for g in d])
    # print(pass_cnt)
    return int(pass_cnt / len(d) * 100)

T = [0 for i in range(5)]
R = [0 for i in range(5)]
T[0] = "codility1"
T[1] = "codility3"
T[2] = "codility2"
T[3] = "codility4b"
T[4] = "codility4a"
R[0] = "Wrong answer"
R[1] = "OK"
R[2] = "sdgs"
R[3] = "Runtime error"
R[4] = "OK"

print(solution(T, R))
# "OK"
# "Wrong answer"
# "Time limit exceed"
# "Runtime error"