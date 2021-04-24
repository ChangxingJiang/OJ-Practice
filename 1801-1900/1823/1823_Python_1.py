class Node:
    __slots__ = ("value", "left", "right")

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # 构造双端链表
        head = now = Node(1)
        for i in range(1, n):
            right = Node(i + 1)
            now.right = right
            right.left = now
            now = now.right
        now.right = head
        head.left = now

        # 遍历双端链表直至只剩一个
        now = head
        while n > 1:
            for _ in range(k - 1):
                now = now.right
            left = now.left
            right = now.right
            left.right = right
            right.left = left
            now = right
            n -= 1

        return now.value


if __name__ == "__main__":
    print(Solution().findTheWinner(5, 2))  # 3
    print(Solution().findTheWinner(6, 5))  # 1
