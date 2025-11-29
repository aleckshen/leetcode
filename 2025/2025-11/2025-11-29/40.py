class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def dfs(i, current, total):
            print(current)
            if total == target:
                res.append(list(current))
                return

            if i >= len(candidates) or total > target:
                return 

            current.append(candidates[i])
            dfs(i + 1, current, total + candidates[i])

            current.pop()
            while i + 1 < len(candidates)  and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return res