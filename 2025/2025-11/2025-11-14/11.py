class Solution(object):
    def maxArea(self, height):
        mx = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] <= height[r]:
                mx = max(mx, height[l] * (r - l))
            else:
                mx = max(mx, height[r] * (r - l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return mx