# LeetCode题解(0785)：判断二分图(Python)

题目：[原题链接](https://leetcode-cn.com/problems/is-graph-bipartite/)（中等）

标签：图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (85.10%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        table = [0] * size
        for i in range(size):
            if table[i] != 0:
                continue

            table[i] = 1
            queue = collections.deque([i])
            while queue:
                for _ in range(len(queue)):
                    i1 = queue.popleft()
                    for i2 in graph[i1]:
                        if table[i2] == table[i1]:
                            return False
                        elif table[i2] == 0:
                            table[i2] = table[i1] * (-1)
                            queue.append(i2)

        return True
```

