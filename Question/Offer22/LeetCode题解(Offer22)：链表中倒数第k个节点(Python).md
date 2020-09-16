# LeetCode题解(Offer22)：寻找链表中倒数第k个节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)（简单）

标签：链表、双指针

| 解法           | 时间复杂度          | 空间复杂度 | 执行用时      |
| -------------- | ------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2×N-K)$ = $O(N)$ | $O(1)$     | 52ms (14.13%) |
| Ans 2 (Python) | $O(N)$              | $O(N)$     | 40ms (80.30%) |
| Ans 3 (Python) |                     |            |               |

解法一（双指针）：

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
```

解法二（转换为列表）：

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        lst = []
        while head:
            lst.append(head)
            head = head.next
        return lst[-k]
```