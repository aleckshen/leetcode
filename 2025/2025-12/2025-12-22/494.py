class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo = {}

        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[(i, total)]

        return dfs(0, 0)