class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

    def top(self) -> int:
        """
        Get the top element.
        """

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """


if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
