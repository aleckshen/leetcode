class Solution(object):
    def isInterleave(self, s1, s2, s3):
        memo = {}
        
        def dfs(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if i < len(s1) and s1[i] == s3[k]:
                memo[(i, j, k)] = dfs(i + 1, j, k + 1)
                if memo[(i, j, k)]:
                    return True
                
            if j < len(s2) and s2[j] == s3[k]:
                memo[(i, j, k)] = dfs(i, j + 1, k + 1)
                if memo[(i, j, k)]:
                    return True

            return False

        return dfs(0, 0, 0)