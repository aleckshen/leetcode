class Solution(object):
    def searchMatrix(self, matrix, target):
        outLeft, outRight = 0, len(matrix) - 1

        while outLeft <= outRight:
            outMiddle = (outLeft + outRight) // 2
            row = matrix[outMiddle]

            l, r = 0, len(row) - 1
            while l <= r:
                mid = (r + l) // 2
                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid - 1
                else:
                    return True

            if target > row[-1]:
                outLeft = outMiddle + 1
            elif target < row[0]:
                outRight = outMiddle - 1
            else:
                return False

        return False