from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.put(x)
        for _ in range(self.queue.qsize() - 1):  # 将栈顶元素移动到队头位置
            self.queue.put(self.queue.get())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        ans = self.queue.get()
        self.push(ans)
        return ans

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.queue.empty()


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    obj.empty()
