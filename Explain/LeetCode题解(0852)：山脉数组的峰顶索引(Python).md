# LeetCode题解(0852)：山脉数组的峰顶索引(Python)

题目：[原题链接](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 96ms (76.36%) |
| Ans 2 (Python) | $O(logN)$  | $O(1)$     | 92ms (89.73%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（遍历）：

```python
def peakIndexInMountainArray(self, A: List[int]) -> int:
    for i in range(len(A)):
        if A[i] > A[i + 1]:
            return i
```

解法二（二分查找）：

```python
def peakIndexInMountainArray(self, A: List[int]) -> int:
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```