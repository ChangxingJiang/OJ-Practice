# LeetCode题解(0907)：计算数组的所有子数组的最小值之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-subarray-minimums/)（中等）

标签：栈、栈-单调栈、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 超出时间限制   |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 540ms (72.83%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def sumSubarrayMins(self, A: List[int]) -> int:
    ans = 0
    while A:
        ans += sum(A)
        ans = ans % (10 ** 9 + 7)
        B = []
        for i in range(len(A) - 1):
            B.append(min(A[i], A[i + 1]))
        A = B
    return ans
```

解法二（单调栈）：

```
def sumSubarrayMins(self, A: List[int]) -> int:
    stack = []
    now = 0
    ans = 0  # 当前累加总和
    for i in range(len(A)):
        n = A[i]
        v = 1
        while stack and stack[-1][0] >= n:
            s = stack.pop()
            now -= s[0] * s[1]
            v += s[1]
        now += n * v
        stack.append([n, v])
        ans += now
    return ans
```