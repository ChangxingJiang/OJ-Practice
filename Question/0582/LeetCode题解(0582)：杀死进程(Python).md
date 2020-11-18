# LeetCode题解(0582)：杀死进程(Python)

题目：[原题链接](https://leetcode-cn.com/problems/kill-process/)（中等）

标签：树、队列

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 604ms (29.53%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    class Node:
        def __init__(self, pid):
            self.pid = pid
            self.children = set()

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        nodes = {0: self.Node(0)}

        # 构造节点
        # O(N)
        for i in range(len(pid)):
            nodes[pid[i]] = self.Node(pid[i])

        # 构造树
        # O(N)
        for i in range(len(pid)):
            nodes[ppid[i]].children.add(nodes[pid[i]])

        # 查询进程子树
        ans = []
        node_list = deque([nodes[kill]])
        while node_list:
            node = node_list.popleft()
            ans.append(node.pid)
            for child in node.children:
                node_list.append(child)

        return ans
```