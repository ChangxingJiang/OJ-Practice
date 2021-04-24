# LeetCode题解(LCP31)：变换的迷宫(Python)

题目：[原题链接](https://leetcode-cn.com/problems/Db3wC1/)（困难）

标签：动态规划、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N×M×T)$ | $O(N×M×T)$ | 3264ms (27.32%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        time = len(maze)  # 总时长
        n, m = len(maze[0]), len(maze[0][0])  # 迷宫长宽

        # 当前时间状态矩阵：dp[i][j][k][l]  当前时间到达第(i,j)个位置的迷宫、k=True/False使用了临时消除术、的可选永久消除术使用位置列表
        dp1 = [[[set() for _ in range(2)] for _ in range(m)] for _ in range(n)]
        dp1[0][0][False] = None  # None表示存在尚未使用永久消除术的方法

        # 广度优先搜索方式状态转移：纵坐标、横坐标、是否使用临时消除术
        queue1 = {(0, 0, False)}

        t = 0  # 当前时间变量
        while t < time - 1:
            # 下一个时间结点的状态矩阵
            dp2 = [[[set() for _ in range(2)] for _ in range(m)] for _ in range(n)]
            queue2 = set()

            for i1, j1, use in queue1:  # 提取当前位置

                # 计算当前剩余距离
                d = (n - i1 - 1) + (m - j1 - 1)

                # 如果已经到达终点，则返回True
                if d == 0:
                    return True

                # 计算剩余时间（还能移动的次数）
                s = time - t - 1

                # 如果剩余时间不足，则直接跳过当前情况
                if s - d < 0:
                    continue

                # 生成所有可能的下一步的选择
                maybe_next = []
                if i1 < n - 1:  # 向下走
                    maybe_next.append((i1 + 1, j1))
                if j1 < m - 1:  # 向右走
                    maybe_next.append((i1, j1 + 1))
                if s - d >= 2 and i1 > 0:  # 向上走
                    maybe_next.append((i1 - 1, j1))
                if s - d >= 2 and j1 > 0:  # 向左走
                    maybe_next.append((i1, j1 - 1))
                if s - d >= 1:  # 原地不动
                    maybe_next.append((i1, j1))

                # 遍历所有下一步的选择
                for i2, j2 in maybe_next:
                    if maze[t + 1][i2][j2] == ".":  # 目标位置为空地
                        if dp2[i2][j2][use] is not None:
                            # 判断是否到达终点
                            if i2 == n - 1 and j2 == m - 1:
                                return True

                            if dp1[i1][j1][use] is None:
                                dp2[i2][j2][use] = None
                            else:
                                dp2[i2][j2][use] |= dp1[i1][j1][use]

                            queue2.add((i2, j2, use))
                    else:  # 目标位置为陷阱
                        # 目标位置已经被施展过永久清除术
                        if dp1[i1][j1][use] is not None and (i2, j2) in dp1[i1][j1][use]:
                            # 判断是否到达终点
                            if i2 == n - 1 and j2 == m - 1:
                                return True

                            if dp2[i2][j2][use] is not None:
                                dp2[i2][j2][use].add((i2, j2))

                            queue2.add((i2, j2, use))

                        # 施展临时清除术
                        if use is False:  # 当前还没有施展过临时清除术
                            if dp2[i2][j2][True] is not None:
                                # 判断是否到达终点
                                if i2 == n - 1 and j2 == m - 1:
                                    return True

                                if dp1[i1][j1][use] is None:
                                    dp2[i2][j2][True] = None
                                else:
                                    dp2[i2][j2][True] |= dp1[i1][j1][use]

                                queue2.add((i2, j2, True))

                        # 施展永久清除术
                        if dp1[i1][j1][use] is None:  # 当前存在没有使用过永久清除术的方法
                            # 判断是否到达终点
                            if i2 == n - 1 and j2 == m - 1:
                                return True

                            if dp2[i2][j2][use] is not None:
                                dp2[i2][j2][use].add((i2, j2))

                            queue2.add((i2, j2, use))

            dp1 = dp2
            queue1 = queue2
            t += 1

        return False
```

