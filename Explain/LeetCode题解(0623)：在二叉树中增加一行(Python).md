# LeetCode题解(0623)：在二叉树中增加一行并保留子树方向(Python)

题目：[原题链接](https://leetcode-cn.com/problems/add-one-row-to-tree/)（中等）

标签：树、二叉树、广度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 72ms (53.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # 处理d的值为1的情况
        if d == 1:
            ans = TreeNode(v)
            ans.left = root
            return ans

        d -= 1

        # 层序遍历树到目标行的上一行
        queue = collections.deque([root])
        while d > 1:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            d -= 1

        print(queue)

        # 增加新的一行
        for node in queue:
            if node.left:
                new_node = TreeNode(v)
                new_node.left = node.left
                node.left = new_node
            else:
                node.left = TreeNode(v)
            if node.right:
                new_node = TreeNode(v)
                new_node.right = node.right
                node.right = new_node
            else:
                node.right = TreeNode(v)

        return root
```