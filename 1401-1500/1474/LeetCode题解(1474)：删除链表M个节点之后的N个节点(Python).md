# LeetCode题解(1474)：删除链表M个节点之后的N个节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 68ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = ListNode(0)
        node.next = head
        mm, nn = m, n
        while node:
            if mm:
                node = node.next
                mm -= 1
            elif nn:
                if node.next:
                    node.next = node.next.next
                else:
                    node.next = None
                nn -= 1
            else:
                mm, nn = m, n
        return head
```

