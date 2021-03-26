# LeetCode题解(0886)：可能的二分法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/possible-bipartition/)（中等）

标签：图、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 152ms (75.80%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
def build_graph(edges):
    graph = collections.defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = build_graph(dislikes)

        table = [0] * (N + 1)
        for m1, m2 in dislikes:
            if table[m1] * table[m2] > 0:
                return False
            if table[m1] != 0 or table[m2] != 0:
                continue

            table[m1] = 1

            now = -1
            queue = collections.deque([m1])
            while queue:
                for _ in range(len(queue)):
                    n1 = queue.popleft()
                    for n2 in graph[n1]:
                        if table[n2] == -now:
                            return False
                        elif table[n2] == 0:
                            table[n2] = now
                            queue.append(n2)
                now *= -1

        return True
```

