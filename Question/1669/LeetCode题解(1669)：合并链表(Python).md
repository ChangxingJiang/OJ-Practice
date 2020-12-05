# LeetCode题解(1669)：合并链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/merge-in-between-linked-lists/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(1)$     | 456ms (29.05%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, None
        node = list1
        while node:
            if node.next and node.next.val == a:
                start = node
            if node.val == b:
                end = node.next
            node = node.next

        node = list2
        while node.next:
            node = node.next
        node.next = end
        start.next = list2

        return list1
```