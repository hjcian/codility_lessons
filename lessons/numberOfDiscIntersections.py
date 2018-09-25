from bisect import bisect_right
# def number_of_disc_intersections(A):
#     # write your code in Python 3.6
#     # N = len(A)
#     # count = 0
#     # for i in range(N):
#     #     for j in range(i + 1, N):
#     #         if A[i] + A[j] + i - j > 0:
#     #             count += 1
#     # return count
#     pass
def number_of_disc_intersections(A):
    # https://stackoverflow.com/questions/4801242/algorithm-to-calculate-number-of-intersecting-discs
    pairs = 0
    # create an array of tuples, each containing the start and end indices of a disk
    # some indices may be less than 0 or greater than len(A), this is fine!
    # sort the array by the first entry of each tuple: the disk start indices
    intervals = sorted( [(i-A[i], i+A[i]) for i in range(len(A))] )
    # create an array of starting indices using tuples in intervals
    print(intervals)
    starts = [i[0] for i in intervals]
    # for each disk in order of the *starting* position of the disk, not the centre
    for i in range(len(starts)):
        # find the end position of that disk from the array of tuples
        disk_end = intervals[i][1]
        # find the index of the rightmost value less than or equal to the interval-end
        # this finds the number of disks that have started before disk i ends
        count = bisect_right(starts, disk_end)
        print(i, count)
        # subtract current position to exclude previous matches
        # this bit seemed 'magic' to me, so I think of it like this...
        # for disk i, i disks that start to the left have already been dealt with
        # subtract i from count to prevent double counting
        # subtract one more to prevent counting the disk itsself
        # 因為是用start point來排序，所以每一個區間用binary search找到的所有start比第i個end point還低的區間，
        # 一定包含i+1個，也就是一定會算到自己 + 前面i個，因為前面i的start point都比你的start還早，故你的end一定比他的start還晚
        count -= i + 1
        pairs += count
        if pairs > 10000000:
            return -1
    return pairs


A = [1,5,2,1,4,0]
# A = [3, 0, 1, 6]
r = number_of_disc_intersections(A)
print(r)