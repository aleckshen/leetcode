class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        result = []

        for word in strs:
            sort = "".join(sorted(word))
            if sort in anagrams:
                anagrams[sort].append(word)
            else:
                anagrams[sort] = [word]

        for list in anagrams.values():
            result.append(list)

        return result
    
strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(result)
        