# LeetCode题解(1035)：不相交的线(Python)

题目：[原题链接](https://leetcode-cn.com/problems/uncrossed-lines/)（中等）

标签：数组、动态规划、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(A×B)$   | $O(A×B)$   | 340ms (8.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)

        @functools.lru_cache(None)
        def dfs(i1, i2):
            if i1 == n1 or i2 == n2:
                return 0
            if A[i1] == B[i2]:
                return 1 + dfs(i1 + 1, i2 + 1)
            else:
                return max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))

        return dfs(0, 0)
```

