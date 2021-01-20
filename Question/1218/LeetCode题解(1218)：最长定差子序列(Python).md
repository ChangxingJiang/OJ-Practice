# LeetCode题解(1218)：最长定差子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/)（中等）

标签：动态规划、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 660ms (50.69%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        count = collections.Counter()

        for n in arr:
            if n - difference in count:
                count[n] = count[n - difference] + 1
            else:
                count[n] = 1
            ans = max(ans, count[n])
        return ans
```

