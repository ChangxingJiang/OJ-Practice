# LeetCode题解(0977)：有序数组的平方(Python)

题目：[原题链接](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 240ms (98.34%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 304ms (41.04%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic排序法）：

```python
def sortedSquares(self, A: List[int]) -> List[int]:
    return sorted([a*a for a in A])
```

解法二（双指针）：

```python
def sortedSquares(self, A: List[int]) -> List[int]:
    size = len(A)

    idx2 = 0
    while idx2 < size and A[idx2] < 0:
        idx2 += 1
    idx1 = idx2 - 1

    ans = []
    while 0 <= idx1 and idx2 <= size - 1:
        p1 = A[idx1] ** 2
        p2 = A[idx2] ** 2
        if p1 < p2:
            ans.append(p1)
            idx1 -= 1
        else:
            ans.append(p2)
            idx2 += 1

    while 0 <= idx1:
        ans.append(A[idx1] ** 2)
        idx1 -= 1

    while idx2 <= size - 1:
        ans.append(A[idx2] ** 2)
        idx2 += 1

    return ans
```