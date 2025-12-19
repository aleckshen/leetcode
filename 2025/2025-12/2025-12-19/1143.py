class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i, j)] = max(dfs(i, j + 1), dfs(i + 1, j))

            return memo[(i, j)] 

        return dfs(0, 0)