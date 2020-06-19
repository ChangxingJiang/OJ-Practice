# LeetCode题解(0206)：翻转单链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-linked-list/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 44ms ( >73.78%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（迭代并反转链表）：

```python
def reverseList(self, head: ListNode) -> ListNode:
    node = None
    while head:
        temp = ListNode(head.val)
        temp.next = node
        node = temp
        head = head.next
    return node
```