class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}

        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 0

        return False
    
nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)
print(result)