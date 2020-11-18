# LeetCode题解(0431)：将N叉树编码为二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/encode-n-ary-tree-to-binary-tree/)（困难）

标签：树、N叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 96ms (37.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        # 处理空树的情况
        if not root:
            return None

        # 递归处理
        head = TreeNode(root.val)
        head.right = TreeNode(None)
        p = head.right
        if root.children:
            for c in root.children:
                p.left = self.encode(c)
                p = p.left
        return head

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        # 处理空树的情况
        if not data:
            return None

        # 递归处理
        root = Node(val=data.val, children=[])
        data = data.right
        while data.left:
            root.children.append(self.decode(data.left))
            data = data.left
        return root
```