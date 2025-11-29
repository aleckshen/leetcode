class Solution(object):
    def permute(self, nums):
        res = []
        permutation = []
        visited = set()

        def dfs():
            if len(permutation) == len(nums):
                res.append(list(permutation))
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                permutation.append(nums[i])

                dfs()

                permutation.pop()
                visited.remove(i)

        dfs()
        return res