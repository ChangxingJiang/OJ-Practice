# LeetCode题解(0545)：二叉树的边界(Python)

题目：[原题链接](https://leetcode-cn.com/problems/boundary-of-binary-tree/)（中等）

标签：树、二叉树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 52ms (82.56%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        # 寻找左边界
        left = []
        node = root
        if node.left:
            while node:
                left.append(node)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        else:
            # 根不存在左子树，故根自身即为左边界
            left = [root]

        # 寻找右边界
        right = []
        node = root
        if node.right:
            while node:
                right.append(node)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        else:
            # 根不存在右子树，故根自身即为右边界
            right = [root]
        right.reverse()

        # 寻找叶子节点
        leaf = []

        def dfs(node):
            if node:
                if node.left or node.right:
                    dfs(node.left)
                    dfs(node.right)
                else:
                    leaf.append(node)

        dfs(root)

        # print([p.val for p in left])
        # print([p.val for p in leaf])
        # print([p.val for p in right])

        # 处理只有一个节点的情况
        if left == leaf == right:
            return [p.val for p in left]

        # 合成结果
        ans = []

        if left[-1] == leaf[0]:
            ans += [p.val for p in left[:-1]]
        else:
            ans += [p.val for p in left]

        if leaf[-1] == right[0]:
            ans += [p.val for p in leaf[:-1]]
        else:
            ans += [p.val for p in leaf]

        if right[-1] == left[0]:
            ans += [p.val for p in right[:-1]]
        else:
            ans += [p.val for p in right]

        return ans
```