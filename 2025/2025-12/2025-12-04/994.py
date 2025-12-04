import collections

class Solution(object):
    def orangesRotting(self, grid):
        minutes = 0
        fresh = 0

        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r - 1 >= 0 and grid[r - 1][c] == 1: #top
                    grid[r - 1][c] = 2
                    queue.append((r - 1, c))
                    fresh -= 1
                if c - 1 >= 0 and grid[r][c - 1] == 1: #left
                    grid[r][c - 1] = 2
                    queue.append((r, c - 1))
                    fresh -= 1
                if r + 1 < rows and grid[r + 1][c] == 1: #bottom
                    grid[r + 1][c] = 2
                    queue.append((r + 1, c))
                    fresh -= 1
                if c + 1 < cols and grid[r][c + 1] == 1: #right
                    grid[r][c + 1] = 2
                    queue.append((r, c + 1))
                    fresh -= 1

            minutes += 1

        if fresh == 0:
            return minutes
        return -1