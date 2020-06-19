# LeetCode题解(0203)：删除链表中的所有指定值元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-linked-list-elements/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 76ms (>74.15%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（建立头结点，使处理第一个结点和中间节点没有区别）：

```python
def removeElements(self, head: ListNode, val: int) -> ListNode:
    ans = node = ListNode(0)
    ans.next = node.next = head
    while node and node.next:
        while node.next and node.next.val == val:
            node.next = node.next.next
        node = node.next
    return ans.next
```

