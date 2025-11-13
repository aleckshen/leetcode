class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [] # (index, height) pairs
        mx = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                mx = max(mx, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            mx = max(mx, h * (len(heights) - i))

        return mx