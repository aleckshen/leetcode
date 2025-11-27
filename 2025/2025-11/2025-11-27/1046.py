import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            if heaviest == stones[0]:
                heapq.heappop(stones)
                continue

            heapq.heappush(stones, heaviest - heapq.heappop(stones))
 
        if not stones:
            return 0
        
        return -stones[0]