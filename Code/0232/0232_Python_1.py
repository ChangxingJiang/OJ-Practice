from queue import LifoQueue


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stark = LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stark.put(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        temp = LifoQueue()
        for _ in range(self.stark.qsize() - 1):
            temp.put(self.stark.get())

        ans = self.stark.get()

        for _ in range(temp.qsize()):
            self.stark.put(temp.get())
        return ans

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stark.qsize() != 0:
            temp = LifoQueue()
            for _ in range(self.stark.qsize() - 1):
                temp.put(self.stark.get())

            ans = self.stark.get()

            self.stark.put(ans)
            for _ in range(temp.qsize()):
                self.stark.put(temp.get())

            return ans

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.stark.qsize() == 0


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
