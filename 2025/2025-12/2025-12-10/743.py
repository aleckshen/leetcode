import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        edges = { i:[] for i in range(1, n + 1)}
        for node, neighbour, weight in times:
            edges[node].append((neighbour, weight))

        minHeap = [(0, k)]
        visited = set()
        time = 0
        
        while minHeap:
            currWeight, currNode = heapq.heappop(minHeap)
            if currNode in visited:
                continue

            visited.add(currNode)
            time = max(time, currWeight)

            for node, weight in edges[currNode]:
                if node not in visited:
                    heapq.heappush(minHeap, (weight + currWeight, node))

        if len(visited) == n:
            return time
        return -1