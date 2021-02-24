# LeetCode题解(1462)：课程安排IV(Python)

题目：[原题链接](https://leetcode-cn.com/problems/course-schedule-iv/)（中等）

标签：图、拓扑排序、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N+P+Q)$ | $O(N+P)$   | 124ms (98.84%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # ---------- 构造图 ----------
        graph_in = collections.defaultdict(set)
        graph_out = collections.defaultdict(set)
        for edge in prerequisites:
            graph_out[edge[0]].add(edge[1])
            graph_in[edge[1]].add(edge[0])

        # ---------- 拓扑排序 ----------
        count = [0] * n
        # 统计所有节点的入射边
        for idx in graph_in:
            count[idx] = len(graph_in[idx])

        # 初始节点
        queue = collections.deque()
        for idx in range(len(count)):
            if count[idx] == 0:
                queue.append(idx)

        table = [set() for _ in range(n)]

        # 拓扑排序
        while queue:
            idx1 = queue.pop()
            for idx2 in graph_out[idx1]:
                table[idx2] |= {idx1}
                table[idx2] |= table[idx1]
                count[idx2] -= 1
                if count[idx2] == 0:
                    queue.append(idx2)

        ans = []
        for idx1, idx2 in queries:
            ans.append(idx1 in table[idx2])
        return ans
```

