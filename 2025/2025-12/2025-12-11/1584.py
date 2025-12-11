import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        adj = { i:[] for i in range(len(points))} #(weight, node) pairs
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                dist = abs(x - x1) + abs(y - y1)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visited = set()
        minHeap = [(0, 0)]

        while len(visited) < len(points):
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res += weight
            for neiWeight, neiNode in adj[node]:
                heapq.heappush(minHeap, (neiWeight, neiNode))

        return res