# LeetCode题解(1019)：链表中的下一个更大的节点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/next-greater-node-in-linked-list/)（中等）

标签：链表、栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 404ms (27.93%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 352ms (85.11%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def nextLargerNodes(self, head: ListNode) -> List[int]:
    stack = []
    ans = []
    idx = 0
    while head:
        ans.append(0)
        while stack and head.val > stack[-1][0]:
            ans[stack.pop()[1]] = head.val
        stack.append([head.val, idx])
        idx += 1
        head = head.next
    return ans
```

解法二（逆序）：

```python
def nextLargerNodes(self, head: ListNode) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next

    stack = []
    for i in range(len(values) - 1, -1, -1):
        while stack and values[i] >= stack[-1]:
            stack.pop()
        stack.append(values[i])
        if len(stack) > 1:
            values[i] = stack[-2]
        else:
            values[i] = 0
    return values
```



