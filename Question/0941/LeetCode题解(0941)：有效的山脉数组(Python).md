# LeetCode题解(0941)：有效的山脉数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/valid-mountain-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 256ms (67.37%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 252ms (76.14%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（单向遍历）：

```python
def validMountainArray(self, A: List[int]) -> bool:
    up = 0
    down = 0
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            if down:
                return False
            up += 1
        elif A[i] > A[i + 1]:
            down += 1
        else:
            return False
    return up > 0 and down > 0
```

解法二（双向遍历）：

```python
def validMountainArray(self, A: List[int]) -> bool:
    idx1 = 0
    idx2 = len(A) - 1
    while idx1 < idx2:
        if A[idx1] < A[idx1 + 1]:
            idx1 += 1
        elif A[idx2 - 1] > A[idx2]:
            idx2 -= 1
        else:
            return False
    return idx1 != 0 and idx2 != len(A) - 1
```