# LeetCode题解(Offer24)：反转链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (14.20%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 44ms (77.44%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            ans = ListNode(0)
            ans.next = head
            node = head.next
            head.next = None
            while node:
                temp = ans.next
                ans.next = node
                node = node.next
                ans.next.next = temp
            return ans.next
```

解法二（合并解法一的指针交换）：

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            ans = ListNode(0)
            ans.next, node, head.next = head, head.next, None
            while node:
                ans.next, node.next, node = node, ans.next, node.next
            return ans.next
```