# LeetCode题解(1130)：中序遍历的叶值的最小代价生成树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values/)（中等）

标签：栈、栈-单调栈、二叉树、二叉树-遍历、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (79.51%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

```python
def mctFromLeafValues(self, arr: List[int]) -> int:
    ans = 0
    stack = []
    for n in arr:
        if not stack or stack[-1] > n:
            stack.append(n)
        else:
            while stack:
                top = stack.pop()
                if stack and stack[-1] <= n:
                    ans += top * stack[-1]
                else:
                    ans += top * n
                    stack.append(n)
                    break
    while len(stack) > 1:
        ans += stack.pop() * stack[-1]
    return ans
```