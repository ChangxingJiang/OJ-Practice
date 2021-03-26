# LeetCode题解：0002（两数相加）

题目：[原题链接](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)（中等）

标签：链表、链表-头结点、链表-双链表

| 解法           | 时间复杂度    | 空间复杂度    | 执行用时       |
| -------------- | ------------- | ------------- | -------------- |
| Ans 1 (Python) | $O(max(m,n))$ | $O(max(m,n))$ | 76ms (>60.58%) |
| Ans 2 (Python) | $O(max(m,n))$ | $O(max(m,n))$ | 64ms (>96.98%) |

## 解法一（按位依次相加）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode(0)  # 返回结果
    carry = 0  # 进位计数
    node = ans  # 当前位
    while True:
        value = carry
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        node.val = value % 10
        carry = value // 10
        if l1 or l2 or carry == 1:
            node.next = ListNode(0)
            node = node.next
        else:
            break
    return ans
```

## 解法二（优化代码结构）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(None)  # 返回结果 当前节点
    now = 0  # 进位计数
    while l1 or l2 or now:
        now += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        node.next = ListNode(now % 10)
        node = node.next
        now //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return ans.next
```



