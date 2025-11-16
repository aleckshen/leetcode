class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        longest = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest