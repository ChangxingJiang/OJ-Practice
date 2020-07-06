from toolkit import ListNode


class Node(ListNode):
    def __init__(self, val, prev, next, child):
        super().__init__(val)
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


if __name__ == "__main__":
    pass
