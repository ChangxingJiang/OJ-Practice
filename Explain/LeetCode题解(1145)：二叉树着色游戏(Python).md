# LeetCode题解(1145)：判断二叉树着色游戏是否有必胜策略(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-coloring-game/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (68.89%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.choose_3 = -1  # 二号玩家选项3：一号玩家的右子节点
        self.choose_2 = -1  # 二号玩家选项2：一号玩家的左子节点
        self.choose_1 = -1  # 二号玩家选项1：一号玩家的父节点

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def dfs(node):
            if not node:
                return 0
            if node.val == x:
                self.choose_2 = dfs(node.left)
                self.choose_3 = dfs(node.right)
                self.choose_1 = n - self.choose_2 - self.choose_3 - 1
                return self.choose_2 + self.choose_3 + 1
            else:
                return dfs(node.left) + dfs(node.right) + 1

        dfs(root)

        point2 = max(self.choose_1, self.choose_2, self.choose_3)
        point1 = sum([self.choose_1, self.choose_2, self.choose_3]) - point2

        return point2 > point1
```