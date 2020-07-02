# LeetCode题解(0908)：数组加任意数后极值的最小差值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-range-i/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 148ms (63.71%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 160ms (36.49%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
def smallestRangeI(self, A: List[int], K: int) -> int:
    return max(max(A) - min(A) - 2 * K, 0)
```

解法二（遍历）：

```python
def smallestRangeI(self, A: List[int], K: int) -> int:
    maximum = float("-inf")
    minimum = float("inf")
    for a in A:
        if a > maximum:
            maximum = a
        if a < minimum:
            minimum = a
    ans = maximum - minimum - 2 * K
    if ans > 0:
        return ans
    else:
        return 0
```