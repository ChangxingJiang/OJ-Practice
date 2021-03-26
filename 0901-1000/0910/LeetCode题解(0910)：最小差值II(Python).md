# LeetCode题解(0910)：最小差值II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-range-ii/)（中等）

标签：贪心算法、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(logN)$  | 196ms (27.84%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        min_val, max_val = A[0], A[-1]
        ans = max_val - min_val
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(max_val - K, a + K) - min(min_val + K, b - K))
        return ans
```

