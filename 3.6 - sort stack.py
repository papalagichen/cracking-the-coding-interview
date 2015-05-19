class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        return self.data.pop() if len(self.data) > 0 else None

    def peek(self):
        return self.data[-1] if len(self.data) > 0 else None

    def isEmpty(self):
        return len(self.data) == 0


def sort_stack(s1):
    s2 = Stack()
    while not s1.isEmpty():
        x = s1.pop()
        while not s2.isEmpty() and s2.peek() < x:
            s1.push(s2.pop())
        s2.push(x)
    while not s2.isEmpty():
        s1.push(s2.pop())


if __name__ == '__main__':
    import Test

    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(2)
    s.push(4)
    s.push(6)

    sort_stack(s)

    Test.equal(6, s.pop())
    Test.equal(5, s.pop())
    Test.equal(4, s.pop())
    Test.equal(3, s.pop())
    Test.equal(2, s.pop())
    Test.equal(1, s.pop())
