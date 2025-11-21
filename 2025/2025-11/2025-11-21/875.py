import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            totalTime = 0
            for banana in piles:
                totalTime += math.ceil(float(banana) / k)

            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res