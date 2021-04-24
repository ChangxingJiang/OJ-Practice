# LeetCode题解(0310)：最小高度树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-height-trees/)（中等）

标签：图、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 88ms (72.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 处理1个节点的特殊情况
        if n == 1:
            return [0]
        # 处理2个结点的特殊情况
        if n == 2:
            return [0, 1]

        # 构造图，并统计每个节点的相邻节点数量
        graph = collections.defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        # 广度优先搜索队列
        queue = collections.deque()
        for i, edge in graph.items():
            if len(edge) == 1:
                queue.append(i)

        while queue:
            n -= len(queue)
            for _ in range(len(queue)):
                # 能遍历到i时，说明i只有一条邻边
                i = queue.popleft()
                j = graph[i].pop()
                graph[j]._remove(i)
                if len(graph[j]) == 1:
                    queue.append(j)

            if n == 1 or n == 2:
                return list(queue)
```

