class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.size += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self.size -= 1
        return self.stack.pop(self.size)

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.size != 0:
            return self.stack[self.size - 1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.size == 0


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.pop())
    obj.empty()
