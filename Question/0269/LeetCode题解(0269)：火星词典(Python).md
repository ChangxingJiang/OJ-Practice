# LeetCode题解(0269)：火星词典(Python)

题目：[原题链接](https://leetcode-cn.com/problems/alien-dictionary/)（困难）

标签：图、拓扑排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (76.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.prev = set()
            self.next = set()

        def __repr__(self):
            return self.val

    def __init__(self):
        self.graph = {}

    def alienOrder(self, words: List[str]) -> str:
        # 初始化图
        for word in words:
            for ch in word:
                if ch not in self.graph:
                    self.graph[ch] = self._Node(ch)

        # 按字母位置增加关联
        visited = {words[0][0]}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # 防止重复出现
                    if w2[:j + 1] in visited:
                        return ""
                    visited.add((w2[:j + 1]))

                    # print("CONNECT:", w1[j], "->", w2[j])
                    if self.graph[w2[j]] in self.graph[w1[j]].prev:
                        return ""
                    if self.graph[w1[j]] in self.graph[w2[j]].next:
                        return ""
                    self.graph[w1[j]].next.add(self.graph[w2[j]])
                    self.graph[w2[j]].prev.add(self.graph[w1[j]])
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        # 拓扑排序
        order = self.order()

        return "".join(order)

    def order(self):
        count = {}  # 节点入射边统计
        queue = []  # 当前入射边为0的节点列表

        # 统计所有节点的入射边
        for node in self.graph.values():
            count[node] = len(node.prev)
            if count[node] == 0:
                queue.append(node)

        # 拓扑排序
        order = []
        while queue:
            node = queue.pop()
            order.append(node.val)
            for next in node.next:
                count[next] -= 1
                if count[next] == 0:
                    queue.append(next)
            # print(queue, count)

        return order
```