# LeetCode题解(1659)：最大化网格幸福感(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximize-grid-happiness/)（困难）

标签：动态规划、回溯算法、记忆化递归

| 解法           | 时间复杂度       | 空间复杂度   | 执行用时        |
| -------------- | ---------------- | ------------ | --------------- |
| Ans 1 (Python) | $O(M×N×I×E×3^N)$ | $O(M×N×3^N)$ | 2572ms (35.90%) |
| Ans 2 (Python) |                  |              |                 |
| Ans 3 (Python) |                  |              |                 |

解法一：

```python
class Solution:
    def __init__(self):
        self.m, self.n = 0, 0

        # 压缩状态的定义
        self.masks = {}  # 记录每一个状态的三进制表示
        self.truncate = {}  # 下一位的三种情况

    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        self.m, self.n = m, n

        # 预处理状态压缩的情况
        highest = 3 ** (n - 1)
        for mask in range(3 ** n):
            mask_tmp = mask
            bits = []
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            self.masks[mask] = bits[::-1]
            self.truncate[mask] = [mask % highest * 3, mask % highest * 3 + 1, mask % highest * 3 + 2]

        return self.dfs(0, 0, introvertsCount, extrovertsCount)

    @lru_cache(None)
    def dfs(self, pos: int, borderline: int, nx: int, wx: int):
        """深度优先遍历：记忆化递归"""
        # 边界条件：如果已经分配到结尾，或已经分配了的所有人
        if pos == self.m * self.n or nx + wx == 0:
            return 0

        # 什么都不做
        best = self.dfs(pos + 1, self.truncate[borderline][0], nx, wx)
        # 放一个内向的人
        if nx > 0:
            best = max(best, 120 + self.count(1, self.masks[borderline][0]) \
                       + (0 if pos % self.n == 0 else self.count(1, self.masks[borderline][self.n - 1])) \
                       + self.dfs(pos + 1, self.truncate[borderline][1], nx - 1, wx))
        # 放一个外向的人
        if wx > 0:
            best = max(best, 40 + self.count(2, self.masks[borderline][0]) \
                       + (0 if pos % self.n == 0 else self.count(2, self.masks[borderline][self.n - 1])) \
                       + self.dfs(pos + 1, self.truncate[borderline][2], nx, wx - 1))

        return best

    @staticmethod
    def count(x, y):
        """计算相邻的房屋x和房屋y之间的收益增量"""
        if x == 0 or y == 0:  # 有一个空房
            return 0
        elif x == 1 and y == 1:  # 两个内向的人
            return -60
        elif x == 2 and y == 2:  # 两个外向的人
            return 40
        else:  # 一个外向的人和一个内向的人
            return -10
```

