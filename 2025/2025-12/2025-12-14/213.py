class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        dp1 = [0] * len(nums)
        dp1[1] = nums[1]

        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])
        
        return max(dp[-2], dp1[-1])