# LeetCode题解(0739)：计算想要观测到更高气温所需等待的天数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/daily-temperatures/)（中等）

标签：栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 512ms (96.60%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

```python
def dailyTemperatures(self, T: List[int]) -> List[int]:
    size = len(T)
    ans = [0] * size
    stack = []
    for i in range(size - 1, -1, -1):
        while stack and T[stack[-1]] < T[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1] - i
        stack.append(i)
    return ans
```