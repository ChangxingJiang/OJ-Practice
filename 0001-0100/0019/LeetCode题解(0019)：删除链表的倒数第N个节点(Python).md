# LeetCode题解(0019)：删除链表的倒数第N个节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)（中等）

标签：链表-双指针、链表-遍历

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (81.69%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    node, curr = head, head
    for _ in range(n + 1):
        if not curr:
            return head.next
        curr = curr.next
    while curr:
        node = node.next
        curr = curr.next
    node.next = node.next.next
    return head
```