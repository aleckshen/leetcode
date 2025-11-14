class Solution(object):
    def maxProfit(self, prices):
        mx = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            mx = max(mx, prices[r] - prices[l])
            r += 1

        return mx