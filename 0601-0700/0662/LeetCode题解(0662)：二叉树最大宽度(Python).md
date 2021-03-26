# LeetCode题解(0662)：计算二叉树的最大宽度(每层的宽度为最左节点和最右节点之间的长度)(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-width-of-binary-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (62.76%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 44ms (91.59%) |
| Ans 3 (Python) |            |            |               |

解法一（修改二叉树存值）：

```python
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 处理根节点为空的情况
        if not root:
            return 0

        ans = 0
        queue = collections.deque([root])
        while queue:
            # 计算当前层的宽度
            min_idx = queue[0].val
            max_idx = queue[-1].val
            ans = max(ans, max_idx - min_idx + 1)

            # 寻找下一层的节点并将节点的值赋为节点坐标
            for _ in range(len(queue)):
                node = queue.popleft()
                idx = node.val
                if node.left:
                    node.left.val = idx * 2 - 1
                    queue.append(node.left)
                if node.right:
                    node.right.val = idx * 2
                    queue.append(node.right)

        return ans
```

解法二（不修改二叉树存值）：

```python
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # 处理根节点为空的情况
        if not root:
            return 0

        ans = 0
        queue = collections.deque([(root, 1)])
        while queue:
            # 计算当前层的宽度
            min_idx = queue[0][1]
            max_idx = queue[-1][1]
            ans = max(ans, max_idx - min_idx + 1)

            # 寻找下一层的节点并将节点的值赋为节点坐标
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, idx * 2 - 1))
                if node.right:
                    queue.append((node.right, idx * 2))

        return ans
```