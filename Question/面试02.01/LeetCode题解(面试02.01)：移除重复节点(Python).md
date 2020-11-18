# LeetCode题解(面试02.01)：移除链表中的重复节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-duplicate-node-lcci/)（简单）

标签：链表、集合

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 80ms (91.93%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head

        lst = {head.val}
        node = head
        while node.next:
            if node.next.val not in lst:
                lst.add(node.next.val)
                node = node.next
            else:
                node.next = node.next.next
        return head
```