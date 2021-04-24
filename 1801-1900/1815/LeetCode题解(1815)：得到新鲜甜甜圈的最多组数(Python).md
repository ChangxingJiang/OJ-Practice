# LeetCode题解(1815)：得到新鲜甜甜圈的最多组数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts/)（困难）

标签：动态规划、记忆化递归

| 解法           | 时间复杂度   | 空间复杂度   | 执行用时        |
| -------------- | ------------ | ------------ | --------------- |
| Ans 1 (Python) | $O(4^2×5^6)$ | $O(4^2×5^6)$ | 1416ms (43.06%) |
| Ans 2 (Python) |              |              |                 |
| Ans 3 (Python) |              |              |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.cache = {}

    def maxHappyGroups(self, batch_size: int, groups: List[int]) -> int:
        if batch_size == 1:
            return len(groups)

        ans = 0

        count = [0] * batch_size  # 统计每种余数的数量
        for group in groups:
            remainder = group % batch_size
            if remainder == 0:
                ans += 1
            else:
                count[remainder] += 1

        # 所有可以除尽的组最先安排，一定都是开心的
        def dfs(stat, rest):
            key = (tuple(stat), rest)
            if key in self.cache:
                return self.cache[key]

            res = 0
            for i in range(1, batch_size):
                if stat[i] > 0:
                    stat[i] -= 1
                    if rest == 0:
                        res = max(res, dfs(stat, (rest + i) % batch_size) + 1)
                    else:
                        res = max(res, dfs(stat, (rest + i) % batch_size))
                    stat[i] += 1

            self.cache[key] = res

            return res

        return ans + dfs(count, 0)
```

