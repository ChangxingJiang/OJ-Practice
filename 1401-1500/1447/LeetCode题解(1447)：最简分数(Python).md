# LeetCode题解(1447)：最简分数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/simplified-fractions/)（中等）

标签：数学

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时       |
| -------------- | ------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(1)$     | 104ms (73.83%) |
| Ans 2 (Python) |              |            |                |
| Ans 3 (Python) |              |            |                |

解法一：

```python
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1:
                    ans.append(str(i) + "/" + str(j))
        return ans
```

