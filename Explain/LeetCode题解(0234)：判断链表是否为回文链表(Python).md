# LeetCode题解(0234)：判断链表是否为回文链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-linked-list/)（简单）

标签：链表、链表-双指针、链表-快慢针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (90.22%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 136ms (5.85%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 92ms (39.29%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（转换为列表比较）：

```python
def isPalindrome(self, head: ListNode) -> bool:
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums == nums[::-1]
```

解法二（翻转链表实现）：

```python
def isPalindrome(self, head: ListNode) -> bool:
    if head is None or head.next is None:
        return True

    # 定位到链表中点（奇数个为绝对中点，偶数个为中线右侧）
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 翻转链表中点后半段链表
    reverse = None
    while slow:
        temp = ListNode(slow.val)
        temp.next = reverse
        reverse = temp
        slow = slow.next
    # print(reverse, head)

    # 比较翻转后的后半段链表与前半段链表是否相同（如果为奇数则最后一次比较中点和中点自己是否相同）
    while reverse:
        if reverse.val != head.val:
            # print(reverse.val, head.val)
            return False
        head = head.next
        reverse = reverse.next
    else:
        return True
```

解法三（解法二整理）：

```python
def isPalindrome(self, head: ListNode) -> bool:
    # 寻找链表中点（快慢针法）
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 翻转后半部分链表
    reverse = None
    while slow:
        node = ListNode(slow.val)
        node.next = reverse
        reverse = node
        slow = slow.next

    # 比较链表是否相同
    while reverse:
        if reverse.val != head.val:
            return False
        head = head.next
        reverse = reverse.next
    else:
        return True
```