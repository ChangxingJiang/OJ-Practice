# LeetCode题解(0143)：重排链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reorder-list/)（中等）

标签：链表、链表-双指针、链表-快慢针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 140ms (17.17%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 104ms (79.31%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 104ms (79.31%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def reorderList(self, head: ListNode) -> None:
    # 处理特殊情况
    if not head or not head.next:
        return

    # 寻找链表中点
    slow = fast = head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 翻转链表后半部分
    curr = slow.next
    while curr and curr.next:
        now = ListNode(curr.next.val)
        now.next = slow.next
        slow.next = now
        curr.next = curr.next.next

    # 重排链表
    node = head
    while node != slow and slow.next:
        now = ListNode(slow.next.val)
        now.next = node.next
        node.next = now
        node = node.next.next
        slow.next = slow.next.next
```

解法二（双指针，减少插入和删除的次数）：

```python
def reorderList(self, head: ListNode) -> None:
    # 处理特殊情况
    if not head or not head.next:
        return

    # 寻找链表中点
    slow = fast = head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 移除后半部分链表
    curr = slow.next
    slow.next = None

    # 翻转链表后半部分
    reverse = None
    while curr:
        point = curr.next
        curr.next = reverse
        reverse = curr
        curr = point

    # 重排链表
    while head and head.next:
        point = reverse.next
        reverse.next = head.next
        head.next = reverse
        head = head.next.next
        reverse = point
    if reverse:
        head.next = reverse
```

解法三（修改链表中点处理方法）：

```python
def reorderList(self, head: ListNode) -> None:
    # 处理特殊情况
    if not head or not head.next:
        return

    # 寻找链表中点
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # 移除后半部分链表
    curr = slow.next
    slow.next = None

    # 翻转链表后半部分
    reverse = None
    while curr:
        curr.next, reverse, curr = reverse, curr, curr.next

    # 重排链表
    while reverse:
        reverse.next, head.next, head, reverse = head.next, reverse, head.next, reverse.next
```