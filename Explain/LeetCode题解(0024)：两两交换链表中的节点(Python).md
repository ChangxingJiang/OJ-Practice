# LeetCode题解(0024)：两两交换链表中的节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (74.11%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def swapPairs(self, head: ListNode) -> ListNode:
    ans = node = ListNode(0)
    ans.next = head
    while node.next and node.next.next:
        node1 = node.next
        node2 = node.next.next
        node1.next = node2.next
        node2.next = node1
        node.next = node2
        node = node.next.next
    return ans.next
```