# LeetCode题解：0141（环形链表）

题目：[题目链接](https://leetcode-cn.com/problems/linked-list-cycle/)（简单）

标签：链表、链表-环形链表、链表-双指针、链表-快慢针

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 60ms (>73.78%) |
| Ans 2 (Python) | 56ms (>87.48%) |

解法一（使用哈希表实现）：

```python
def hasCycle(self, head: ListNode) -> bool:
    hashset = set()
    while head:
        if head in hashset:
            return True
        else:
            hashset.add(head)
            head = head.next
    return False
```

解法二（快慢指针法：不循环一定会结束，循环一定会相遇）：

```python
def hasCycle(self, head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```