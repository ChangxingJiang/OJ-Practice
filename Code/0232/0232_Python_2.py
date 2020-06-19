class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stark = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stark.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stark.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stark[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stark) == 0


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
