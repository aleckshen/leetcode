class Solution(object):
    def checkValidString(self, s):
        left = []
        star = []

        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            elif char == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop() 

        while left and star:
            if star[-1] > left[-1]:
                left.pop()
            star.pop()

        return not left