# LeetCode题解(1253)：重构2行二进制矩阵(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix/)（中等）

标签：贪心算法、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 100ms (80.95%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        size = len(colsum)

        count2 = colsum.count(2)
        count1 = colsum.count(1)
        upper -= count2
        lower -= count2
        if upper + lower != count1 or upper < 0 or lower < 0:
            return []

        ans = [[0] * size for _ in range(2)]

        for i in range(size):
            if colsum[i] == 2:
                ans[0][i] = ans[1][i] = 1
            elif colsum[i] == 1:
                if upper:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1

        return ans
```

