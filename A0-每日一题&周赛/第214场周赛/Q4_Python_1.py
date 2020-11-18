import random
from typing import List


class SkipList:
    class Node:
        __slots__ = ["val", "next", "prev", "below", "above", "distance"]

        def __init__(self, val, next=None, prev=None, below=None, above=None, distance=1):
            self.val = val
            self.next = next
            self.prev = prev
            self.below = below
            self.above = above
            self.distance = distance  # 到右侧的距离

    def __init__(self, height=17):
        self.height = height

        self.head = self.Node(float("-inf"))
        self.head.next = self.Node(float("inf"))
        self.head.next.prev = self.head

        node = self.head
        for _ in range(height - 1):
            node.below = self.Node(float("-inf"))
            node.below.above = node
            node.below.next = self.Node(float("inf"))
            node.below.next.above = node.next
            node.below.next.prev = node.below.next
            node = node.below

    def _search(self, val, now=None):
        if not now:
            now = self.head

        while now.below:
            now = now.below
            while val >= now.next.val:
                now = now.next

        return now

    def find(self, val):
        return self._search(val)

    def insert(self, val):
        left = self._search(val)
        right = left.next

        node = self.Node(val)
        node.prev = left
        node.next = right

        right.prev = node
        left.next = node

        height = 1
        while height < self.height and random.randint(0, 1):
            height += 1

    def random_height(self):
        height = 1
        while random.randint(0, 1):
            height += 1
            if height == self.height:
                break
        return height


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:


if __name__ == "__main__":
    print(Solution().createSortedArray(instructions=[1, 5, 6, 2]))  # 1
    print(Solution().createSortedArray(instructions=[1, 2, 3, 6, 5, 4]))  # 3
    print(Solution().createSortedArray(instructions=[1, 3, 3, 3, 2, 4, 2, 1, 2]))  # 4
