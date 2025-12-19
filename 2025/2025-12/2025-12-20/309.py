class Solution(object):
    def maxProfit(self, prices):
        memo = {} #(index, buying) pairs

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            cooldown = dfs(i + 1, buying)    
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
                return memo[(i, buying)]
            else:
                sell = dfs(i + 2, True) + prices[i]
                memo[(i, buying)] = max(sell, cooldown)
                return memo[(i, buying)]

        return dfs(0, True)