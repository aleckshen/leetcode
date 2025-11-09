class Solution(object):
    def longestConsecutive(self, nums):
        hashSet = set(nums)
        longestSeq = 0

        for num in hashSet:
            if (num - 1) not in hashSet:
                length = 1
                while (num + length) in hashSet:
                    length += 1
                longestSeq = max(length, longestSeq)

        return longestSeq

nums = [100,4,200,1,3,2]   
solution = Solution()
result = solution.longestConsecutive(nums)
print(result)