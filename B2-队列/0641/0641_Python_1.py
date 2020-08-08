class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """


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
