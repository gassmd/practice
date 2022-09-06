from intervaltree import Interval


class Solution(object):
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:        # neetcode solution
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:        # if new interval has end value less than start value of current interval       i.e  newIv = [2, 4], iIv = [5, 6]
                res.append(newInterval)                 # add new interval to list
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:      # if start value of new interval is greater than end value of current interval
                res.append(intervals[i])
            else:                                       # else new interval is overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]     # takes min of both and max of both for new interval
        res.append(newInterval)
        return res

    def insert1(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right

test_intervals1 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval1 = [4, 8]
test1 = Solution().insert(intervals=test_intervals1, newInterval=new_interval1)
test11 = Solution().insert1(intervals=test_intervals1, newInterval=new_interval1)

print(test11)