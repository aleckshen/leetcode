class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = []

        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            if prevInterval[1] >= intervals[i][0]:
                prevInterval = [min(prevInterval[0], intervals[i][0]),
                                max(prevInterval[1], intervals[i][1])]
            else:
                res.append(prevInterval)
                prevInterval = intervals[i]

        if res and res[-1][1] > prevInterval[0]:
            res[-1] = [min(prevInterval[0], res[-1][0]),
                       max(prevInterval[1], res[-1][1])]
        else:
            res.append(prevInterval)

        return res