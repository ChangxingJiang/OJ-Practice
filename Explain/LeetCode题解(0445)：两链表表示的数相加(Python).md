# LeetCode题解(0445)：两链表表示的数相加(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-two-numbers-ii/)（中等）

标签：链表、链表-双指针、栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 88ms (71.38%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 88ms (71.38%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（双指针+数组存储结点指针）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 计算l1的长度
    size1 = 0
    node1 = l1
    while node1:
        node1 = node1.next
        size1 += 1
    node1 = l1

    # 计算l2的长度
    size2 = 0
    node2 = l2
    while node2:
        node2 = node2.next
        size2 += 1
    node2 = l2

    maximum = max(size1, size2)

    ans = node = ListNode(0)
    stack = [node]
    for i in range(maximum, 0, -1):
        value = 0
        if size1 >= i:
            value += node1.val
            node1 = node1.next
        if size2 >= i:
            value += node2.val
            node2 = node2.next

        if value >= 10:
            for j in range(len(stack) - 1, -1, -1):
                stack[j].val += 1
                if stack[j].val == 10:
                    stack[j].val = 0
                else:
                    break

        node.next = ListNode(value % 10)
        node = node.next
        stack.append(node)

    if ans.val:
        return ans
    else:
        return ans.next
```

解法二（用栈做逆序处理）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    stack1 = []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next

    stack2 = []
    while l2:
        stack2.append(l2.val)
        l2 = l2.next

    ans = None
    carry = 0
    while stack1 or stack2 or carry > 0:
        n1 = stack1.pop() if stack1 else 0
        n2 = stack2.pop() if stack2 else 0
        value = n1 + n2 + carry
        carry = value // 10
        node = ListNode(value % 10)
        node.next = ans
        ans = node

    return ans
```