# LeetCode题解(0296)：最佳的碰头地点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-meeting-point/)（困难）

标签：数学、排序、广度优先搜索、图

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时       |
| -------------- | ------------------------ | ---------- | -------------- |
| Ans 1 (Python) | $O(N×M×P)$ : 其中P为人数 | $O(N×M)$   | 超出时间限制   |
| Ans 2 (Python) | $O(N×M)$                 | $O(N×M)$   | 60ms (100.00%) |
| Ans 3 (Python) |                          |            |                |

解法一：

```python
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < s1 and 0 <= y < s2

        def get_near(x, y):
            res = []
            for xx, yy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if is_valid(xx, yy):
                    res.append((xx, yy))
            return res

        if not grid or not grid[0]:
            return 0

        s1, s2 = len(grid), len(grid[0])

        people = []
        for i1 in range(s1):
            for i2 in range(s2):
                if grid[i1][i2] == 1:
                    people.append((i1, i2))

        dp = [[0] * s2 for _ in range(s1)]
        for person in people:
            visited = {person}
            queue = collections.deque([person])
            distance = 0
            while queue:
                distance += 1
                for _ in range(len(queue)):
                    (i1, i2) = queue.popleft()
                    for (j1, j2) in get_near(i1, i2):
                        if (j1, j2) not in visited:
                            visited.add((j1, j2))
                            queue.append((j1, j2))
                            dp[j1][j2] += distance

        return min(min(dp[i1]) for i1 in range(s1))
```

解法二：

```python
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:

        # 已知每个值的分布数时计算中位数
        def get_median(lst):
            vv = sum(lst)
            if len(lst) % 2 == 0:
                m1, m2 = vv // 2 - 1, vv // 2
                v1, v2 = -1, -1
                last = 0
                for i in range(len(lst)):
                    last += lst[i]
                    if last > m1 and v1 == -1:
                        v1 = i
                    if last > m2:
                        v2 = i
                        break
                return (v1 + v2) / 2
            else:
                m = vv // 2
                last = 0
                for i in range(len(lst)):
                    last += lst[i]
                    if last > m:
                        return i

        # 最终的位置一定在横纵的中位数的位置上

        s1, s2 = len(grid), len(grid[0])

        # 统计行
        # O(N)
        count_row = []
        for i1 in range(s1):
            count_row.append(sum(grid[i1]))

        # 统计列
        # O(M)
        count_col = []
        for i2 in range(s2):
            count_col.append(sum(grid[i1][i2] for i1 in range(s1)))

        # O(N)
        people_num = sum(count_row)

        # 计算行的中位数
        # O(N)
        row_median = get_median(count_row)

        # 计算列的中位数
        # O(N)
        col_median = get_median(count_col)

        # print(count_row, row_median)
        # print(count_col, col_median)

        ans = 0

        # 计算行的总值
        # O(N)
        for i1 in range(s1):
            ans += abs(row_median - i1) * count_row[i1]

        # 计算列的总值
        for i2 in range(s2):
            ans += abs(col_median - i2) * count_col[i2]

        return int(ans)
```