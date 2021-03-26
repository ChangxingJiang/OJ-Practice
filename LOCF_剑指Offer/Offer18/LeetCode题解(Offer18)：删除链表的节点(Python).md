# LeetCode题解(Offer18)：删除链表中的指定节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (95.90%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        else:
            node = head
            while node.next:
                if node.next.val == val:
                    node.next = node.next.next
                    return head
                node = node.next
```