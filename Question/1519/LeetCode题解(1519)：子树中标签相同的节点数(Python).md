# LeetCode题解(1519)：子树中标签相同的节点数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)（中等）

标签：图、深度优先搜索、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1996ms (49%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Node:
    def __init__(self, i, val):
        self.i = i
        self.val = val
        self.near = set()


class Solution:
    def __init__(self):
        self.ans = []

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # 生成节点字典
        # O(N)
        node_dict = {i: Node(i, labels[i]) for i in range(n)}

        # 生成图的连通结构
        # O(N)
        for edge in edges:
            node1, node2 = node_dict[edge[0]], node_dict[edge[1]]
            node1.near.add(node2)
            node2.near.add(node1)

        # 遍历树结构计算结果
        # 时间:O(N) 空间:O(N)

        self.ans = [0] * n

        def dfs(last_node, now_node):
            res = [0] * 26
            res[ord(now_node.val) - 97] += 1
            for next_node in now_node.near:
                if next_node != last_node:
                    temp = dfs(now_node, next_node)
                    for i in range(26):
                        res[i] += temp[i]
            self.ans[now_node.i] = res[ord(now_node.val) - 97]
            return res

        dfs(None, node_dict[0])

        return self.ans
```