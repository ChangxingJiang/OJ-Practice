class MyLinkedList:
    class _Node:
        """"""
        __slots__ = "value", "next"

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value) + "->" + str(self.next)

    def __init__(self):
        self._head = self._Node(0)
        self._size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            return -1
        curr = self._head
        for _ in range(index + 1):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self._size:
            return
        self._size += 1
        prev = self._head
        for _ in range(index):
            prev = prev.next
        node = self._Node(val, prev.next)
        prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._size:
            return
        self._size -= 1
        prev = self._head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next


if __name__ == "__main__":
    # 测试用例1
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    print(linkedList.get(1))  # 2
    linkedList.deleteAtIndex(1)
    print(linkedList.get(1))  # 3

    # 测试用例2
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.deleteAtIndex(0)

    # 测试用例3
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtHead(7)
    linkedList.addAtHead(2)
    linkedList.addAtIndex(3, 0)
    linkedList.deleteAtIndex(2)
    linkedList.addAtHead(6)
    linkedList.addAtTail(4)
    print(linkedList.get(4))
    linkedList.addAtHead(4)
    linkedList.addAtIndex(5, 0)
    linkedList.addAtHead(6)

    # 测试用例4
    linkedList = MyLinkedList()
    linkedList.addAtHead(4)
    print(linkedList.get(1))
    linkedList.addAtHead(1)
    linkedList.addAtHead(5)
    linkedList.deleteAtIndex(3)
    linkedList.addAtHead(7)
    print(linkedList.get(3))
    print(linkedList.get(3))
    print(linkedList.get(3))
    linkedList.addAtHead(1)
    linkedList.deleteAtIndex(4)
