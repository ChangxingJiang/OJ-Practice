# LeetCode题解(0212)：单词搜索II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-search-ii/)（困难）

标签：回溯算法、字典树、深度优先搜索

| 解法           | 时间复杂度    | 空间复杂度 | 执行用时       |
| -------------- | ------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(M×N×26^L)$ | $O(M×N)$   | 9848ms (5.06%) |
| Ans 2 (Python) |               |            |                |
| Ans 3 (Python) |               |            |                |

解法一：

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构造字典树
        root = {}
        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word

        m, n = len(board), len(board[0])

        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        def neighbors(x, y):
            return [(xx, yy) for xx, yy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if is_valid(xx, yy)]

        # 深度优先搜索
        def dfs(now, i1, j1, visited):
            if board[i1][j1] not in now:
                return
            now = now[board[i1][j1]]
            if "#" in now:
                ans.add(now["#"])
            for i2, j2 in neighbors(i1, j1):
                if (i2, j2) not in visited:
                    visited.add((i2, j2))
                    dfs(now, i2, j2, visited)
                    visited._remove((i2, j2))

        ans = set()

        # 遍历二维网格
        for i in range(m):
            for j in range(n):
                dfs(root, i, j, {(i, j)})

        return list(ans)
```

