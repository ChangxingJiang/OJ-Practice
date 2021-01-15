# LeetCode题解(0133)：克隆图(Python)

题目：[原题链接](https://leetcode-cn.com/problems/clone-graph/)（中等）

标签：图、广度优先搜索、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (33.23%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # 构造所有新节点以及新旧节点对应表
        hashmap = {}
        queue = collections.deque([node])
        visited = {node}
        while queue:
            old = queue.popleft()
            new = Node(val=old.val)
            hashmap[old] = new
            for neighbor in old.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        # 构造所有新节点之间的关系
        for old, new in hashmap.items():
            for neighbor in old.neighbors:
                new.neighbors.append(hashmap[neighbor])

        return hashmap[node]
```

