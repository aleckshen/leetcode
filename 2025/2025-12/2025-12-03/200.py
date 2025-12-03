class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            dfs(i + 1, j) #bottom
            dfs(i, j + 1) #right
            dfs(i - 1, j) #top
            dfs(i, j - 1) #left

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
                else:
                    continue

        return islands