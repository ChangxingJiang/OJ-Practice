# LeetCode题解(0237)：删除链表中给定的结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(1)       | O(1)       | 48s (>78.76%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（因无法获取上一个结点，只能将当前结点替换为下一个结点）：

```python
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
```