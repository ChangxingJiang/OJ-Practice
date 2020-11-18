# LeetCode题解(面试02.02)：返回链表倒数第k个结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/)（简单）

标签：链表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 32ms (96.84%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        i1, i2 = head, head

        for _ in range(k - 1):
            i1 = i1.next

        while i1.next:
            i1 = i1.next
            i2 = i2.next

        return i2.val
```