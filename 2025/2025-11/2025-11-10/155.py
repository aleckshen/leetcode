class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val):
        if not self.minimum or val < self.minimum[-1] or val == self.minimum[-1]:
            self.minimum.append(val)
        self.stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.minimum[-1]:
                self.minimum.pop()
            self.stack.pop()
        
    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        if self.minimum:
            return self.minimum[-1]