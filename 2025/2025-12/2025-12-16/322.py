class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]

            res = float('inf')
            for coin in coins:
                if total - coin >= 0:
                    res = min(res, 1 + dfs(total - coin))

            memo[total] = res
            return res

        minCoins = dfs(amount)
        if minCoins == float('inf'):
            return -1
        return minCoins