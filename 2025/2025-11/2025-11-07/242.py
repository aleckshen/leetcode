class Solution(object):
    def isAnagram(self, s, t):
        dic_s = {}
        dic_t = {}

        for letter in s:
            if letter in dic_s:
                dic_s[letter] += 1
            else:
                dic_s[letter] = 1

        for letter in t:
            if letter in dic_t:
                dic_t[letter] += 1
            else:
                dic_t[letter] = 1
                
        return dic_s == dic_t

s = "a"
t = "aa"
solution = Solution()
result = solution.isAnagram(s, t)
print(result)