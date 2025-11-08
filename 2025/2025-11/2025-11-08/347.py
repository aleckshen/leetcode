class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        tuple_list = []
        result = []
        k_count = 0

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for value, freq in dic.items():
            tuple_list.append((freq, value))

        tuple_list.sort()
        
        for freq, value in tuple_list[::-1]:
            if k_count == k:
                break
            result.append(value)
            k_count += 1

        return result

nums = [1,1,1,2,2,3] 
k = 2  
solution = Solution()
result = solution.topKFrequent(nums, k)
print(result)