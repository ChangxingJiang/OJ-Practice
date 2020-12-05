# LeetCode题解(0399)：除法求值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/evaluate-division/)（中等）

标签：图、并查集、深度优先搜索

| 解法           | 时间复杂度               | 空间复杂度 | 执行用时      |
| -------------- | ------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(Q×N)$ : 其中N为变量数 | $O(N)$     | 40ms (62.76%) |
| Ans 2 (Python) |                          |            |               |
| Ans 3 (Python) |                          |            |               |

解法一：

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        params = set(p1 for p1, p2 in equations) | set(p2 for p1, p2 in equations)
        size = len(equations)

        # 构造图
        graph = {param: {} for param in params}
        for i in range(size):
            (x, y), value = equations[i], values[i]
            graph[x][y] = value
            graph[y][x] = 1 / value

        def dfs(n1, n3, visited, now=1):
            for n2 in graph[n1]:
                if n2 not in visited:
                    if n2 == n3:
                        return now * graph[n1][n2]
                    else:
                        v = dfs(n2, n3, visited=visited | {n2}, now=now * graph[n1][n2])
                        if v != -1:
                            return v
            return -1

        # 深度优先搜索解题
        ans = []
        for x, y in queries:
            if x not in graph or y not in graph:
                ans.append(-1)
            elif x == y:
                ans.append(1)
            else:
                ans.append(dfs(x, y, visited={x}))

        return ans
```