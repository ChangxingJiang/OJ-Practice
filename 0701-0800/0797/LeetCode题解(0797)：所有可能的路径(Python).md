# LeetCode题解(0797)：所有可能的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/all-paths-from-source-to-target/)（中等）

标签：回溯算法、图、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N!)$    | 47ms (85.53%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def dfs(path):
            if path[-1] == n - 1:
                ans.append(list(path))
            else:
                for nxt in graph[path[-1]]:
                    path.append(nxt)
                    dfs(path)
                    path.pop()

        dfs([0])

        return ans
```

