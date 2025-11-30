class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(list(subset))
                return

            subset.append(nums[i])
            dfs(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res