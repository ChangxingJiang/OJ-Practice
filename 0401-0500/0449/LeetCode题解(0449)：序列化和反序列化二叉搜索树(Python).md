# LeetCode题解(0449)：“将二叉搜索树序列化为文本”与“从文本反序列化为二叉搜索树”(Python)

题目：[原题链接](https://leetcode-cn.com/problems/serialize-and-deserialize-bst/)（中等）

标签：树、二叉树、二叉搜索树、广度优先搜索、设计

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (99.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

![LeetCode题解(0449)：截图](LeetCode题解(0449)：截图.png)

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 处理根节点为空的情况
        if not root:
            return "[]"

        # 处理根节点不为空的情况
        ans = [str(root.val)]
        now_node = [root]
        while now_node:
            next_node = []
            for node in now_node:
                if node.left:
                    next_node.append(node.left)
                    ans.append(str(node.left.val))
                else:
                    ans.append("null")
                if node.right:
                    next_node.append(node.right)
                    ans.append(str(node.right.val))
                else:
                    ans.append("null")
            now_node = next_node

        while ans[-1] == "null":
            ans.pop()

        return "[" + ",".join(ans) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 处理根节点为空的情况
        if data == "[]":
            return None

        # 拆分根节点
        data = data[1:-1].split(",")
        size = len(data)
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        i = 1
        while i < size:
            node = queue.popleft()
            if data[i] != "null":
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            if i + 1 < size and data[i + 1] != "null":
                node.right = TreeNode(int(data[i + 1]))
                queue.append(node.right)
            i += 2
        return root
```