class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.index = 0
        self.count = 0
        self.size = k

    def insertFront(self, value: int) -> bool:
        if self.count < self.size:
            idx = (self.size + self.index - 1) % self.size
            self.queue[idx] = value
            self.index = idx
            self.count += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.size:
            idx = (self.index + self.count) % self.size
            self.queue[idx] = value
            self.count += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.count > 0:
            self.index = (self.index + 1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            self.count -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.count > 0:
            return self.queue[self.index]
        else:
            return -1

    def getRear(self) -> int:
        if self.count > 0:
            idx = (self.index + self.count - 1) % self.size
            return self.queue[idx]
        else:
            return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)
    print(circularDeque.insertLast(1))  # True
    print(circularDeque.insertLast(2))  # True
    print(circularDeque.insertFront(3))  # True
    print(circularDeque.insertFront(4))  # False
    print(circularDeque.getRear())  # 2
    print(circularDeque.isFull())  # True
    print(circularDeque.deleteLast())  # True
    print(circularDeque.insertFront(4))  # True
    print(circularDeque.getFront())  # 4
