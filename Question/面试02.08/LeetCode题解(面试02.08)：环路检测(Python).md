# LeetCode题解(面试02.08)：寻找链表与环的交点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/linked-list-cycle-lcci/)（中等）

标签：链表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (62.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        i1 = i2 = head

        # 快慢针寻找环
        while i2.next and i2.next.next:
            i2 = i2.next.next
            i1 = i1.next
            if i1 == i2:
                break
        else:
            return None

        # 双指针寻找入环交点
        i3 = head
        while i1 != i3:
            i1 = i1.next
            i3 = i3.next

        return i1
```