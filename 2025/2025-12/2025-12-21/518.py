class Solution(object):
    def change(self, amount, coins):
        memo = {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i >= len(coins):
                return 0
            if total > amount:
                return 0
            if total == amount:
                return 1

            memo[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)   
            return memo[(i, total)] 

        return dfs(0, 0)