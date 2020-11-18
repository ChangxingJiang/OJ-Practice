# LeetCode题解(面试02.03)：删除链表的中间节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-middle-node-lcci/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 48ms (79.14%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```