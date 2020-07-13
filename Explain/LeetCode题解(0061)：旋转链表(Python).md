# LeetCode题解(0061)：旋转链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rotate-list/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (91.04%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (91.04%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针）：

```python
def rotateRight(self, head: ListNode, k: int) -> ListNode:

    if not head:
        return None

    size = 0
    node = head
    while node:
        node = node.next
        size += 1

    k = k % size

    start = head

    ans = node = ListNode(0)

    for _ in range(size - k):
        node.next = ListNode(start.val)
        node = node.next
        start = start.next

    node = ans
    while start:
        now = ListNode(start.val)
        now.next = node.next
        node.next = now
        node = node.next
        start = start.next

    return ans.next
```

解法二（直接将新首尾相连）：

```python
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    # 处理特殊情况
    if not head:
        return None

    # 将链表的队尾的指针指向链表的队头
    size = 1
    node = head
    while node.next:
        node = node.next
        size += 1
    node.next = head

    # 计算新的队头位置
    k = k % size

    # 将新的队尾指向空，并返回新的队头
    node = head
    for _ in range(size - k - 1):
        node = node.next
    ans = node.next
    node.next = None

    return ans
```