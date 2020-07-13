# LeetCode题解(0092)：部分反转链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-linked-list-ii/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) |            |            | 32ms (97.17%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    # 处理特殊情况
    if not head:
        return None

    # 找到翻转部分的前一个元素
    ans = node = ListNode(0)
    ans.next = head
    for _ in range(m - 1):
        node = node.next

    # 翻转链表
    curr = node.next
    for _ in range(n - m):
        now = ListNode(curr.next.val)
        now.next = node.next
        node.next = now
        curr.next = curr.next.next

    return ans.next
```