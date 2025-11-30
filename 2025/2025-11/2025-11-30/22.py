class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def dfs(string, openn, closed):
            if openn == n == closed:
                res.append(string)
                return
            
            if openn < n:
                dfs(string + "(", openn + 1, closed)

            if closed < n and closed < openn:
                dfs(string + ")", openn, closed + 1)

        dfs("", 0, 0)
        return res