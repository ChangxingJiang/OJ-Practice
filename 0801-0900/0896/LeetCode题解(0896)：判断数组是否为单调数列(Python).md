# LeetCode题解(0896)：判断数组是否为单调数列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/monotonic-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 604ms (60.47%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 608ms (57.81%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（遍历）：

```python
def isMonotonic(self, A: List[int]) -> bool:
    ans = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            if ans > 0:
                return False
            ans = -1
        elif A[i] < A[i + 1]:
            if ans < 0:
                return False
            ans = 1
    else:
        return True
```

解法二（Pythonic）：

```python
def isMonotonic(self, A: List[int]) -> bool:
    B = sorted(A)
    return B == A or B == A[::-1]
```