from toolkit import ListNode


class Node(ListNode):
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        super().__init__(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        pass


if __name__ == "__main__":
    pass
