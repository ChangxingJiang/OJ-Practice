# LeetCode题解(面试02.04)：分割链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-list-lcci/)（中等）

标签：链表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (84.11%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1 = node1 = ListNode(0)
        head2 = node2 = ListNode(0)

        while head:
            if head.val >= x:
                node2.next = ListNode(head.val)
                node2 = node2.next
            else:
                node1.next = ListNode(head.val)
                node1 = node1.next
            head = head.next

        node1.next = head2.next

        return head1.next
```