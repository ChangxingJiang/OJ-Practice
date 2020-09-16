# LeetCode题解(0147)：对链表进行插入排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/insertion-sort-list/)（中等）

标签：链表、链表-双指针、排序、排序-插入排序

说明：这道题不要去和那些直接sort排序的人比，时间复杂度摆在这儿呢，比不过的。

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 1796ms (28.65%) |
| Ans 2 (Python) | $O(N^2)$   | $O(N)$     | 224ms (65.98%)  |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def insertionSortList(self, head: ListNode) -> ListNode:
    # 处理特殊情况
    if not head or not head.next:
        return head

    # 插入排序
    ans = ListNode(float("-inf"))
    node = head
    while node:
        # 寻找插入位置
        curr = ans
        while curr.next and curr.next.val < node.val:
            curr = curr.next

        # 执行插入
        point = node.next
        node.next = curr.next
        curr.next = node
        node = point

    return ans.next
```

解法二（因此测试数据存在1-4999升序排列的链表，对此作出如下修改，如测试数据正常，这样的修改未必能提高效率）：

```python
def insertionSortList(self, head: ListNode) -> ListNode:
    # 处理特殊情况
    if not head or not head.next:
        return head

    # 插入排序
    ans = ListNode(float("-inf"))
    last = ans
    node = head
    while node:
        # 寻找插入位置
        if last.val < node.val:
            point = node.next
            node.next = None
            last.next = node
            last = last.next
            node = point
        else:
            curr = ans
            while curr.next and curr.next.val < node.val:
                curr = curr.next

            # 执行插入
            point = node.next
            node.next = curr.next
            curr.next = node
            node = point

    return ans.next
```