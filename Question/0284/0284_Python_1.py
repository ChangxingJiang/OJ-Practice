class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.top = None

    def peek(self):
        if not self.top:
            self.top = self.iterator.next()
        return self.top

    def next(self):
        if not self.top:
            return self.iterator.next()
        else:
            ans, self.top = self.top, None
            return ans

    def hasNext(self):
        if self.top:
            return True
        else:
            return self.iterator.hasNext()



if __name__ == "__main__":
    obj = PeekingIterator([1, 2, 3])
    print(obj.next())  # 1
    print(obj.peek())  # 2
    print(obj.next())  # 2
    print(obj.next())  # 3
    print(obj.hasNext())  # False
