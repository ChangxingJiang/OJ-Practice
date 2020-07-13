# LeetCode题解(0082)：删除排序链表中的重复元素(Python)

题目：[原题链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)（中等）

标签：链表、链表-双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (98.18%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def deleteDuplicates(self, head: ListNode) -> ListNode:
    # 处理特殊情况
    if not head:
        return None

    # 遍历删除重复值
    ans = node = ListNode(0)
    while head:
        if not head.next or head.val != head.next.val:
            node.next = ListNode(head.val)
            node = node.next
            head = head.next
        else:
            val = head.val
            while head and head.val == val:
                head = head.next

    return ans.next
```