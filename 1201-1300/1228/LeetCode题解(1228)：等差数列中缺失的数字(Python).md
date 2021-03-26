# LeetCode题解(1228)：等差数列中缺失的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression/)（简单）

标签：数组、排序、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 36ms (89.25%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        d = (arr[-1] - arr[0]) / len(arr)

        ans = 0

        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            v = m * d + arr[0]
            if arr[m] == v:
                ans = v + d
                l = m + 1
            else:
                r = m - 1

        return int(ans)
```