class Solution(object):
    def maxProduct(self, nums):
        dp = [0] * len(nums)
        dp[0] = (nums[0], nums[0]) #(maxProduct, minProduct) pairs

        for i in range(1, len(nums)):
            curr = nums[i]
            prev_max, prev_min = dp[i - 1]

            max_i = max(curr, curr * prev_max, curr * prev_min)
            min_i = min(curr, curr * prev_max, curr * prev_min)

            dp[i] = (max_i, min_i)

        maxProduct = float('-inf')

        for max_i, min_i in dp:
            maxProduct = max(maxProduct, max_i)

        return maxProduct