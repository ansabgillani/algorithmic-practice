class Solution:
    def __init__(self, maxSize):
        self.stack = []
        self.max_size = maxSize

    def push(self, x):
        if len(self.stack) < self.max_size:
            self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else -1

    def increment(self, k, val):
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val