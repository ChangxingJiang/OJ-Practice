# LeetCode题解(1536)：排布二进制网格至目标情况的最少交换次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 56ms (100%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 计算每一行最靠上可以存在的位置
        row_min_idx = []
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    row_min_idx.append(j)
                    break
            else:
                row_min_idx.append(0)

        # print(row_min_idx)

        # 贪心寻找、情景模拟
        ans = 0
        for i in range(n):
            # 如果当前行已符合要求
            if row_min_idx[i] <= i:
                continue

            # 如果当前行不符合要求，寻找符合要求的行
            for j in range(i + 1, n):
                if row_min_idx[j] <= i:
                    ans += j - i
                    row_min_idx = row_min_idx[:i] + [row_min_idx[j]] + row_min_idx[i:j] + row_min_idx[j + 1:]
                    break
            else:
                return -1

        return ans
```