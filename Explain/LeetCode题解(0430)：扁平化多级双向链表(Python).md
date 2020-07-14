# LeetCode题解(0430)：扁平化多级双向链表(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/)（中等）

标签：链表、链表-特殊链表、深度优先遍历

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (59.30%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（递归的深度优先搜索）：

```python
def flatten(self, head: 'Node') -> 'Node':
    # 处理特殊情况
    if not head:
        return head

    # 迭代深度优先搜索
    ans = node = Node(0, None, head, None)
    stack = [head]

    while stack:
        curr = stack.pop()

        node.next = curr
        curr.prev = node

        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None

        node = curr

    ans.next.prev = None
    return ans.next
```