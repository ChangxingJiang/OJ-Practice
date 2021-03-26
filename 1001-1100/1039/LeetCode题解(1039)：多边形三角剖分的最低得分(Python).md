# LeetCode题解(1039)：多边形三角剖分的最低得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon/)（中等）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 132ms (35.11%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def minScoreTriangulation(self, array: List[int]) -> int:
        ans = 0
        while len(array) >= 3:
            max_idx, max_val = 0, 0
            for i, n in enumerate(array):
                if n > max_val:
                    max_idx, max_val = i, n
            ans += array[max_idx - 1] * array[max_idx] * array[(max_idx + 1) % len(array)]
            array.pop(max_idx)
        return ans
```

