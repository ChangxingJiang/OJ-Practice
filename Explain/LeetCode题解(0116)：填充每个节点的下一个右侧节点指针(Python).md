# LeetCode题解(0116)：填充二叉树中每个节点的下一个右侧节点指针(Python)

题目：[原题链接](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (93.71%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 80ms (70.49%) |
| Ans 3 (Python) | $O(N)$     | $O(1)$     | 84ms (52.19%) |

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

        head = root
        while head.left:
            head.left.next = head.right
            node = head
            while node.next:
                node.right.next = node.next.left
                node = node.next
                node.left.next = node.right
            head = head.left

        return root
```

