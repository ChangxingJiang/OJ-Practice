# LeetCode题解(0084)：柱状图中最大的矩形(Python)

题目：[原题链接](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)（困难）

标签：栈、栈-单调栈

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^3)$   | $O(1)$     | 超出时间限制  |
| Ans 2 (Python) | $O(N^2)$   | $O(1)$     | 超出时间限制  |
| Ans 3 (Python) | $O(N)$     | $O(N )$    | 56ms (98.57%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    ans = 0
    for i in range(len(heights)):
        for j in range(i, len(heights)):
            ans = max(ans, (j + 1 - i) * min(heights[i:j + 1]))
    return ans
```

解法二（更好的暴力）：

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    size = len(heights)
    ans = 0
    for i in range(size):
        now = heights[i]
        if now * (size - i) < ans:
            continue
        for j in range(i, size):
            now = min(now, heights[j])
            ans = max(ans, (j + 1 - i) * now)
            if now * (size - i) < ans:
                continue
    return ans
```

解法三（单调栈）：

```python
def largestRectangleArea(self, heights: List[int]) -> int:
    stack = []
    size = len(heights)
    ans = 0
    for i in range(size):
        # 当空栈或栈顶高度小于当前高度时，直接将当前高度压入栈
        if not stack or stack[-1][1] < heights[i]:
            stack.append([i, heights[i]])
        else:
            # 计算当前所有可能的最大值
            now = None
            while stack and stack[-1][1] > heights[i]:
                now = stack.pop()
                ans = max(ans, (i - now[0]) * now[1])
            # 调整当前栈顶情况
            if now:
                stack.append([now[0], heights[i]])

    # 统计剩余的情况
    while stack:
        now = stack.pop()
        ans = max(ans, (size - now[0]) * now[1])

    return ans
```