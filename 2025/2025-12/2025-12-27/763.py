class Solution(object):
    def partitionLabels(self, s):
        res = []

        lastIndex = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in lastIndex:
                lastIndex[s[i]] = i

        size = 0
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end, lastIndex[s[i]])

            if i == end:
                res.append(size)
                end = 0
                size = 0

        return res