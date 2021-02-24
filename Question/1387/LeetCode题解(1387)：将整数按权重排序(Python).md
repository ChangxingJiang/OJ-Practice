# LeetCode题解(1387)：将整数按权重排序(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-integers-by-the-power-value/)（中等）

标签：动态规划、图、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 172ms (94.41%) |
| Ans 2 (Python) | --         | --         | 84ms (97.37%)  |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {1: 0}

        def dfs(x):
            if x not in dp:
                if x % 2 == 1:
                    dp[x] = dfs(x * 3 + 1) + 1
                else:
                    dp[x] = dfs(x // 2) + 1
            return dp[x]

        lst = []
        for i in range(lo, hi + 1):
            v = dfs(i)
            lst.append((v, i))

        lst.sort()

        return lst[k - 1][1]
```

解法二：

```python
DP = {1: 0}


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def dfs(x):
            if x not in DP:
                if x % 2 == 1:
                    DP[x] = dfs(x * 3 + 1) + 1
                else:
                    DP[x] = dfs(x // 2) + 1
            return DP[x]

        lst = []
        for i in range(lo, hi + 1):
            v = dfs(i)
            lst.append((v, i))

        lst.sort()

        return lst[k - 1][1]
```

