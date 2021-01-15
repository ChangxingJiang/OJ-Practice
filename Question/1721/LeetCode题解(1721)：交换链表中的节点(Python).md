# LeetCode题解(1721)：交换链表中的节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 876ms (39.10%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1 = n2 = head
        for _ in range(k - 1):
            n2 = n2.next

        n3 = n2  # 正数第k个节点

        while n2.next:
            n1 = n1.next
            n2 = n2.next

        n4 = n1  # 倒数第k个节点

        n3.val, n4.val = n4.val, n3.val

        return head
```

