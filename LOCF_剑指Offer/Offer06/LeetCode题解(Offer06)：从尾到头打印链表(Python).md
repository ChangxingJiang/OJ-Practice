# LeetCode题解(Offer06)：从尾到头打印链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (55.06%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst[::-1]
```