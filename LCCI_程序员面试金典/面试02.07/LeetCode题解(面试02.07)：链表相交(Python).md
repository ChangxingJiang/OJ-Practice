# LeetCode题解(面试02.07)：寻找两链表的交点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/)（简单）

标签：链表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(1)$     | 172ms (88.35%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（双指针）：

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        i1, i2 = headA, headB
        while i1 or i2:
            if i1 == i2:
                return i1

            i1 = i1.next
            i2 = i2.next

            # 处理未相交的情况
            if i1 is None and i2 is None:
                return None

            if i1 is None:
                i1 = headB
            if i2 is None:
                i2 = headA
```