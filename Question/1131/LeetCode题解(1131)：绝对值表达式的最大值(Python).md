# LeetCode题解(1131)：绝对值表达式的最大值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/)（中等）

标签：数学、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 312ms (68.33%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        x1, x2, x3, x4 = [], [], [], []
        for i in range(len(arr1)):
            x1.append(arr1[i] + arr2[i] + i)
            x2.append(arr1[i] + arr2[i] - i)
            x3.append(arr1[i] - arr2[i] + i)
            x4.append(arr1[i] - arr2[i] - i)
        return max(max(x1) - min(x1), max(x2) - min(x2), max(x3) - min(x3), max(x4) - min(x4))
```



