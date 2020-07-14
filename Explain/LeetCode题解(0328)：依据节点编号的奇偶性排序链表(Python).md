# LeetCode题解(0328)：依据节点编号的奇偶性排序链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/odd-even-linked-list/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (95.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def oddEvenList(self, head: ListNode) -> ListNode:
    odd_head = odd_node = ListNode(0)
    even_head = even_node = ListNode(0)
    is_odd = True
    while head:
        point = head.next
        head.next = None
        if is_odd:
            odd_node.next = head
            odd_node = odd_node.next
        else:
            even_node.next = head
            even_node = even_node.next
        is_odd = not is_odd
        head = point
    odd_node.next = even_head.next
    return odd_head.next
```