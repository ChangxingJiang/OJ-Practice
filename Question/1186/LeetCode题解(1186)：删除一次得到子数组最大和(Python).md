# LeetCode题解(1186)：删除一次得到子数组最大和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 104ms (96.40%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        ans = -10001
        a = b = -10001
        for n in arr:
            a, b = max(a + n, n), max(b + n, a)
            ans = max(ans, a, b)
        return ans
```

