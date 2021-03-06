import sys


class MinStack:
    def __init__(self):
        self.nodes = []
        self.mins = []

    def push(self, x):
        self.nodes.append(x)
        if x <= self.getMin():
            self.mins.append(x)

    def pop(self):
        x = self.nodes.pop()
        if x == self.getMin():
            self.mins.pop()

    def top(self):
        return self.nodes[-1]

    def getMin(self):
        return self.mins[-1] if self.mins else sys.maxint


if __name__ == '__main__':
    import Test

    stack = MinStack()
    stack.push(3)
    stack.push(2)
    stack.push(1)
    Test.test(stack.top, [
        (None, 1)
    ])
    Test.test(stack.getMin, [
        (None, 1)
    ])
    stack.pop()
    Test.test(stack.getMin, [
        (None, 2)
    ])
