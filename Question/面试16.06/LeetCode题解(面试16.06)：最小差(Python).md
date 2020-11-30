# LeetCode题解(面试16.06)：最小差(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-difference-lcci/)（中等）

标签：二分查找、数组、双指针、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 240ms (63.29%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（二分查找）：

```python
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        ans = float("inf")
        for n in b:
            i = bisect.bisect_left(a, n)
            if i < len(a) and a[i] == n:
                return 0
            else:
                if i > 0:
                    ans = min(ans, abs(a[i - 1] - n))
                if i < len(a):
                    ans = min(ans, abs(a[i] - n))
        return ans
```