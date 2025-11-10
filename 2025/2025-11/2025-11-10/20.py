class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in closeToOpen:
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        return True

s = "()"
solution = Solution()
result = solution.isValid(s)
print(result)