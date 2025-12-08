class Solution(object):
    def findRedundantConnection(self, edges):
        adj = [[] for i in range(len(edges) + 1)]

        def dfs(u, parent):
            visited.add(u)
            for v in adj[u]:
                if v == parent:
                    continue
                if v in visited:
                    return True   
                if dfs(v, u):
                    return True
            return False

        visited = set()

        for u, v in edges:
            visited.clear()
            adj[u].append(v)
            adj[v].append(u)

            if dfs(u, -1):
                return [u, v]