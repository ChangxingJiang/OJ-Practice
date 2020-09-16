# LeetCode题解(0652)：寻找二叉树中重复的子树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-duplicate-subtrees/)（中等）

标签：树、二叉树、深度优先搜索、哈希表

| 解法           | 时间复杂度 | 空间复杂度                                  | 执行用时      |
| -------------- | ---------- | ------------------------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(L×H)$ : 其中L为叶节点数量，H为二叉树深度 | 76ms (75.93%) |
| Ans 2 (Python) |            |                                             |               |
| Ans 3 (Python) |            |                                             |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.sub_trees = collections.Counter()
        self.ans = []

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def recursor(node):
            if not node:
                return ""
            if node.left and node.right:
                expression = str(node.val) + ":[" + recursor(node.left) + "," + recursor(node.right) + "]"
            elif node.left:
                expression = str(node.val) + ":[" + recursor(node.left) + ",]"
            elif node.right:
                expression = str(node.val) + ":[," + recursor(node.right) + "]"
            else:
                expression = str(node.val) + ":[,]"
            if self.sub_trees[expression] == 1:
                self.ans.append(node)
            self.sub_trees[expression] += 1
            return expression

        recursor(root)
        return self.ans
```

