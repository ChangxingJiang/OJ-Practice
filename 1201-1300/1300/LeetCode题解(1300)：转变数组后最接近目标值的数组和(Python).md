# LeetCode题解(1300)：转变数组后最接近目标值的数组和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/)（中等）

标签：二分查找、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogT)$ | $O(1)$     | 88ms (35.75%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left, right = 0, max(arr)

        while left < right:
            mid = (left + right) // 2

            res = sum([n if n <= mid else mid for n in arr])

            if res < target:
                left = mid + 1
            elif res > target:
                right = mid
            else:
                return mid

        res1 = sum([n if n <= (left - 1) else (left - 1) for n in arr])
        res2 = sum([n if n <= left else left for n in arr])

        if abs(res1 - target) > abs(res2 - target):
            return left
        else:
            return left - 1
```

