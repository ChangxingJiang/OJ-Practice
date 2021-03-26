# LeetCode题解(1385)：两个数组间的距离值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays/)（简单）

这题相当考语文。

| 解法           | 时间复杂度                               | 空间复杂度 | 执行用时       |
| -------------- | ---------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M)$ : N为arr1长度，M为arr2长度      | $O(1)$     | 100ms (51.84%) |
| Ans 2 (Python) | $O((M+N)logM)$: N为arr1长度，M为arr2长度 | $O(M)$     | 44ms (99.43%)  |
| Ans 3 (Python) |                                          |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    ans = 0
    for a in arr1:
        if all(abs(a - b) > d for b in arr2):
            ans += 1
    return ans
```

解法二（二分查找）：

![LeetCode题解(1385)：截图1](LeetCode题解(1385)：截图1.png)

```python
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()

    ans = 0
    for a in arr1:
        idx = bisect.bisect_left(arr2, a)
        if (idx == 0 or abs(arr2[idx - 1] - a) > d) and (idx == len(arr2) or abs(arr2[idx] - a) > d):
            ans += 1
    return ans
```