# LeetCode题解(0331)：验证二叉树的前序序列化(Python)

题目：[原题链接](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/)（中等）

标签：树、二叉树、二叉树-遍历

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (60.05%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 44ms (60.05%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（栈实现）：

```python
def isValidSerialization(self, preorder: str) -> bool:
    nodes = preorder.split(",")
    stack = []
    i = 0
    while i < len(nodes):
        if nodes[i] != "#":
            stack.append(0)
        else:
            stack[-1] += 1
            while stack and stack[-1] == 2:
                stack.pop()
                if stack:
                    stack[-1] += 1
        i += 1
        if not stack:
            break
    return len(stack) == 0 and i == len(nodes)
```

解法二（槽位计算实现）：

```python
def isValidSerialization(self, preorder: str) -> bool:
    slot = 1
    idx = 0
    while slot > -1 and idx < len(preorder):
        if preorder[idx] == ",":
            slot += 1
        elif preorder[idx] == "#":
            slot -= 2
        idx += 1
    return slot == -1 and idx == len(preorder)
```





