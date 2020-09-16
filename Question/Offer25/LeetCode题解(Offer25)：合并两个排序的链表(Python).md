# LeetCode题解(Offer25)：合并两个排序的链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/)（简单）

标签：链表、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N1+N2)$ | $O(1)$     | 48ms (99.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

![LeetCode题解(Offer25)：截图](LeetCode题解(Offer25)：截图.png)

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l2.next
        if l1 or l2:
            node.next = l1 or l2
        return ans.next
```



