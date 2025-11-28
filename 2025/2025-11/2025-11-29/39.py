class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, current, total):
            if total == target:
                res.append(list(current))
                return

            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])

            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return res