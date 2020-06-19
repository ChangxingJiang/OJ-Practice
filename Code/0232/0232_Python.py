class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """


    def peek(self) -> int:
        """
        Get the front element.
        """


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
