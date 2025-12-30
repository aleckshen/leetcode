def eraseOverlapIntervals(self, intervals):
    intervals.sort()
    count = 0

    prevEnd = intervals[0][1]
    for i in range(1, len(intervals)):
        if prevEnd > intervals[i][0]:
            count += 1
            prevEnd = min(prevEnd, intervals[i][1])
            continue
        prevEnd = intervals[i][1]

    return count