class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def size(self):
        return len(self.s1) + len(self.s2)

    def add(self, x):
        self.s1.append(x)

    def peek(self):
        if len(self.s2) > 0:
            return self.s2[-1]
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def remove(self):
        if len(self.s2) > 0:
            return self.s2.pop()
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        return self.s2.pop()


if __name__ == '__main__':
    import Test

    q = MyQueue()
    q.add(1)
    q.add(2)
    q.add(3)

    Test.equal(3, q.size())
    Test.equal(1, q.peek())
    Test.equal(1, q.remove())
    Test.equal(2, q.remove())
    Test.equal(1, q.size())
    Test.equal(3, q.peek())
