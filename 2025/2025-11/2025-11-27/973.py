import heapq, math

class Solution(object):
    def kClosest(self, points, k):
        maxHeap = []
        res = []

        for point in points:
            distance = math.sqrt((point[0] * point[0]) + (point[1] * point[1]))
            heapq.heappush(maxHeap, (-(distance), point))

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        for tup in maxHeap:
            res.append(tup[1])

        return res