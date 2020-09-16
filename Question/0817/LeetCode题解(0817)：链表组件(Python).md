# LeetCode题解(0817)：链表组件(Python)

题目：[原题链接](https://leetcode-cn.com/problems/linked-list-components/)（中等）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(G)$     | 116ms (98.09%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def numComponents(self, head: ListNode, G: List[int]) -> int:
    G = set(G)
    ans = 0
    part = False
    while head:
        if head.val in G:
            if not part:
                ans += 1
                part = True
        else:
            part = False
        head = head.next
    return ans
```