# LeetCode题解(0086)：依据特定值分隔链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-list/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (95.15%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def partition(self, head: ListNode, x: int) -> ListNode:
    headA = nodeA = ListNode(0)
    headB = nodeB = ListNode(0)
    while head:
        if head.val < x:
            nodeA.next = ListNode(head.val)
            nodeA = nodeA.next
        else:
            nodeB.next = ListNode(head.val)
            nodeB = nodeB.next
        head = head.next
    nodeA.next = headB.next
    return headA.next
```

