# LeetCode题解(0382)：链表随机节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/linked-list-random-node/)（中等）

标签：随机、蓄水池

| 解法           | 时间复杂度                   | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(1)$ ; 随机= $O(N)$ | $O(1)$     | 216ms (47.03%) |
| Ans 2 (Python) |                              |            |                |
| Ans 3 (Python) |                              |            |                |

解法一：

```python
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
```