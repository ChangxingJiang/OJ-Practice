class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.index = 0
        self.count = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count < self.size:
            self.queue[(self.index + self.count) % self.size] = value
            self.count += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count > 0:
            self.index = (self.index + 1) % self.size
            self.count -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count > 0:
            return self.queue[self.index]
        else:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count > 0:
            return self.queue[(self.index + self.count - 1) % self.size]
        else:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.size


if __name__ == "__main__":
    circularQueue = MyCircularQueue(3)
    print(circularQueue.enQueue(1))  # True
    print(circularQueue.enQueue(2))  # True
    print(circularQueue.enQueue(3))  # True
    print(circularQueue.enQueue(4))  # False
    print(circularQueue.Rear())  # 3
    print(circularQueue.isFull())  # True
    print(circularQueue.deQueue())  # True
    print(circularQueue.enQueue(4))  # True
    print(circularQueue.Rear())  # 4
