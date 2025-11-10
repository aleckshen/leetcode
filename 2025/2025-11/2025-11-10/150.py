class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(operand2 - operand1)
            elif token == "/":
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(float(operand2) / operand1))
            else:
                stack.append(int(token))

        return stack.pop()