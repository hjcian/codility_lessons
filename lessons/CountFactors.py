def imperfectSolution(N):
    # write your code in Python 3.6
    # Correctness/Performance: 100/66
    # dead during 780291637 and MAX_INT
    # Detected time complexity: O(sqrt(N)) or O(N), actually is O(N/2), not enough
    if N == 1:
        return 1
    upper_bound = N
    i = 1
    cnt = 0
    while i < upper_bound:
        if N % i == 0:
            upper_bound = N // i
            if N == i * i:
                cnt +=1
            else:
                cnt += 2    
        i += 1
    return cnt

def solution(N):
    cnt = 0
    i = 1
    while ( i * i <= N):
        if (N % i == 0):
            if i * i == N:
                cnt += 1
            else:
                cnt += 2
        i += 1
    return cnt


N = 24
solution(N)