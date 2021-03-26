# LeetCode题解(0117)：填充一般二叉树中每个节点的下一个右侧节点指针 II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 56ms (93.04%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 68ms (41.37%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 64ms (63.95%) |

解法一（层序遍历）：

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 处理特殊情况
        if not root:
            return root

        now_node = [root]
        while now_node:
            last = None
            next_node = []
            for node in now_node:
                node.next = last
                last = node
                if node.right:
                    next_node.append(node.right)
                if node.left:
                    next_node.append(node.left)
            now_node = next_node

        return root
```

解法二（双端队列的层序遍历）：

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 处理特殊情况
        if not root:
            return root

        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
```

解法三（利用已有的next）：

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 处理特殊情况
        if not root:
            return root

        level_left_most = root  # 当前层最左侧的结点
        while True:
            next_level_left_most = None  # 下一行最左侧的节点
            last_node = None  # 当前节点左侧的节点
            node = level_left_most  # 当前层用来遍历的节点
            while node:
                if node.left:
                    if last_node:
                        last_node.next = node.left
                    if not next_level_left_most:
                        next_level_left_most = node.left
                    last_node = node.left
                if node.right:
                    if last_node:
                        last_node.next = node.right
                    if not next_level_left_most:
                        next_level_left_most = node.right
                    last_node = node.right
                node = node.next

            if next_level_left_most:
                level_left_most = next_level_left_most
            else:
                break

        return root
```

