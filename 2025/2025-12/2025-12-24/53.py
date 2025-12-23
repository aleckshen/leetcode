class Solution(object):
    def maxSubArray(self, nums):
        maxSum = float('-inf')

        currSum = 0
        for num in nums:
            currSum += num
            if num > currSum:
                currSum = num
            maxSum = max(maxSum, currSum)

        return maxSum