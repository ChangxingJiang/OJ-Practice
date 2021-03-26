# LeetCode题解(面试02.05)：链表求和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-lists-lcci/)（中等）

标签：链表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(N1+N2)$ | 60ms (97.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(0)
        last = 0  # 进位数量
        while l1 or l2 or last:
            now = last

            if l1:
                now += l1.val
                l1 = l1.next
            if l2:
                now += l2.val
                l2 = l2.next

            last, now = divmod(now, 10)

            node.next = ListNode(now)
            node = node.next

        return head.next
```