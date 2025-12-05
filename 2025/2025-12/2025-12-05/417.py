class Solution(object):
    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or r >= rows 
            or c < 0 or c >= cols or heights[r][c] < prevHeight):
                return 

            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c]) #top
            dfs(r, c - 1, visited, heights[r][c]) #left
            dfs(r + 1, c, visited, heights[r][c]) # bottom
            dfs(r, c + 1, visited, heights[r][c]) # right

        for c in range(cols):
            dfs(0, c, pacific, heights[0][c]) 
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []
        for coord in pacific:
            if coord in atlantic:
                x, y = coord
                res.append([x, y])

        return res