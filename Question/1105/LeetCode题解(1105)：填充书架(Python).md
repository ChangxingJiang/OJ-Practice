# LeetCode题解(1105)：填充书架(Python)

题目：[原题链接](https://leetcode-cn.com/problems/filling-bookcase-shelves/)（中等）

标签：动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×W)$   | $O(N)$     | 76ms (16.11%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        size = len(books)

        dp = [1000000] * (size + 1)
        dp[0] = 0

        for i in range(1, size + 1):
            now_width, now_height = 0, 0
            j = i
            while j > 0:
                now_width += books[j - 1][0]
                now_height = max(now_height, books[j - 1][1])
                if now_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j - 1] + now_height)
                j -= 1

        return dp[-1]
```

