import random

from LeetTool import ListNode
from LeetTool import build_ListNode


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        now = 0
        idx = 0
        node = self.head
        while node:
            idx += 1
            rand = random.randint(1, idx)
            if rand == idx:
                now = node.val
            node = node.next
        return now


if __name__ == "__main__":
    obj = Solution(build_ListNode([1, 2, 3]))
    print(obj.getRandom())  # 1或2或3
