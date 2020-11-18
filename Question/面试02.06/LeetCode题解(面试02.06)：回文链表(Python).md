# LeetCode题解(面试02.06)：判断链表是否为回文链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-linked-list-lcci/)（简单）

标签：链表、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 76ms (86.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（翻转后半部分链表）：

```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        i1 = i2 = head

        # 快慢针求中点
        while i1 and i1.next:
            i1 = i1.next.next
            i2 = i2.next

        # 翻转链表
        i3 = None
        while i2:
            last = i2.next
            i2.next = i3
            i3 = i2
            i2 = last

        # 比较链表
        i4 = head
        while i3 and i4:
            if i3.val != i4.val:
                return False
            i3 = i3.next
            i4 = i4.next

        return True
```