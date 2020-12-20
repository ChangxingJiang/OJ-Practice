# LeetCode题解(0444)：序列重建(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sequence-reconstruction/)（中等）

标签：图、拓扑排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 240ms (23.88%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if len(org) == 1:
            for seq in seqs:
                if seq != [1]:
                    return False
            return [1] in seqs

        size = len(org)

        graph_in = collections.defaultdict(set)
        graph_out = collections.defaultdict(set)
        for seq in seqs:
            for n in seq:
                if n <= 0 or n > size:
                    return False
            for i in range(len(seq) - 1):
                if seq[i] == seq[i + 1]:
                    return False
                graph_in[seq[i + 1]].add(seq[i])
                graph_out[seq[i]].add(seq[i + 1])

        count = {}  # 节点入射边统计
        queue = []  # 当前入射边为0的节点列表

        # 统计所有节点的入射边
        for node in graph_in:
            count[node] = len(graph_in[node])
        for node in graph_out:
            if node not in count:
                count[node] = 0
                queue.append(node)

        # 拓扑排序
        order = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.pop()
            order.append(node)
            for next in graph_out[node]:
                count[next] -= 1
                if count[next] == 0:
                    queue.append(next)

        return order == org
```