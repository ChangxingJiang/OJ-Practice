# LeetCode题解(1575)：统计所有可行路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/count-all-possible-routes/)（困难）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(L^2×F)$ | $O(L×F)$   | 5188ms (22%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一（动态规划）：

```python
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # 城市数量
        city_num = len(locations)

        # 计算各个城市之间的距离
        distances = [[0] * city_num for _ in range(city_num)]
        for i in range(city_num):
            for j in range(i + 1, city_num):
                distances[i][j] = distances[j][i] = abs(locations[i] - locations[j])

        # 初始化都动态规划状态矩阵
        dp = [[0] * city_num for _ in range(fuel + 1)]

        # 将起点设为1
        dp[0][start] = 1

        # 计算状态矩阵
        for i in range(1, fuel + 1):
            for j in range(city_num):
                for k in range(city_num):
                    if k != j:
                        last_fuel = i - distances[j][k]
                        if last_fuel >= 0:
                            dp[i][j] += dp[last_fuel][k]

        # for row in dp:
        #     print(row)

        ans = 0
        for i in range(fuel+1):
            ans += dp[i][finish]

        return ans % (10 ** 9 + 7)
```