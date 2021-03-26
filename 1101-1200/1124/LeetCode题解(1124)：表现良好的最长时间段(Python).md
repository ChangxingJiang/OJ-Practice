# LeetCode题解(1124)：大于特定值的项数超过小于特定值项数的最长连续子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-well-performing-interval/)（中等）

标签：栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 248ms (93.64%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单调栈）：

```python
def longestWPI(self, hours: List[int]) -> int:
    N = len(hours)

    # 计算非零前序和
    total = [0] * (N + 1)
    last = 0
    for i in range(N):
        if hours[i] > 8:
            last += 1
        else:
            last -= 1
        total[i + 1] = last

    # 计算单调栈（所有可能的起始位置）
    stack = []
    for i in range(len(total)):
        if not stack or total[i] < total[stack[-1]]:
            stack.append(i)

    # 计算最终结果
    ans = 0
    for i in range(N, -1, -1):
        while stack and total[stack[-1]] < total[i]:
            ans = max(ans, i - stack[-1])
            stack.pop()

    return ans
```