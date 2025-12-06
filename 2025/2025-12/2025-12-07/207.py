class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        prereqMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visited = set()

        def dfs(course):
            if course in visited:
                return False

            if prereqMap[course] == []:
                return True

            visited.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            prereqMap[course] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True