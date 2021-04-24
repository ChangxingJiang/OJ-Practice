# LeetCode题解(1823)：找出游戏的获胜者(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game/)（中等）

标签：数组、链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 164ms (25.69%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
```

