class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [i, dic[target - nums[i]]]
            else:
                dic[nums[i]] = i

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)
print(result)  
