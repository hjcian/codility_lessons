import numpy as np
IF = {
    "A": 1, 
    "C": 2, 
    "G": 3,
    "T": 4,
}
def violentSolution(S, P, Q):
    # write your code in Python 3.6
    # violent solution
    ret = [IF.get(min(S[p:q+1], key=lambda s: IF.get(s))) for p, q in zip(P, Q)]
    # for p, q in zip(P, Q):
    #     print(S[p:q+1])
    #     minimum = IF.get(min(S[p:q+1], key=lambda s: IF.get(s)))
    #     print(minimum)
    print(ret)

def solution(S, P, Q):
    # https://codesays.com/2014/solution-to-genomic-range-query-by-codility/
    result = []
    DNA_len = len(S)
    mapping = {"A":1, "C":2, "G":3, "T":4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = np.array([[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len])
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    print(next_nucl)
    for index in range(DNA_len - 2, -1, -1):
        next_nucl[0][index] = next_nucl[0][index+1] # 後面的要告訴前面的，我[0]下一次出現在哪個pos
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index # 從S[index]中知道目前是哪個DNA，是最新inclusive的位置
        
    # print(next_nucl)
    #        0  1  2  3  4  5  6
    #        C  A  G  C  C  T  A
    # A   [[ 1  1  6  6  6  6  6]
    # C    [ 0  3  3  3  4 -1 -1]
    # G    [ 2  2  2 -1 -1 -1 -1]
    # T    [ 5  5  5  5  5  5 -1]]
    # 
    for index in range(0, len(P)):
        print(P[index], Q[index])
        print(1, next_nucl[0][P[index]], Q[index])
        print(2, next_nucl[1][P[index]], Q[index])
        print(3, next_nucl[2][P[index]], Q[index])
        print(4, next_nucl[3][P[index]], Q[index])
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
            # 今天[0](i.e. A)是否出現在range P~end，用P[index] != -1來判斷
            # 因P是inclusive，若不在P，表示一定不在P~Q之中
            # 接著再判斷此字符出現的位置是否在Q之前，用P[index] <= Q[index])
            # 若有，則這個range中有出現[0]，也就是IF最小的DNS序列有出現
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
        print(result[-1])
        print("====")
S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]

solution(S, P, Q)