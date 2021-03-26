# LeetCode题解(0025)：K个一组翻转链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)（困难）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 56ms (69.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    ans = node = ListNode(0)
    ans.next = head
    while node:
        # 判断链表剩余长度是否充足
        curr = node
        is_enough = True
        for _ in range(k):
            if curr is None or curr.next is None:
                is_enough = False
                break
            curr = curr.next
        if not is_enough:
            break

        # 翻转链表
        curr = node.next
        for _ in range(k - 1):
            now = ListNode(curr.next.val)
            now.next = node.next
            node.next = now
            curr.next = curr.next.next

        node = curr

    return ans.next
```