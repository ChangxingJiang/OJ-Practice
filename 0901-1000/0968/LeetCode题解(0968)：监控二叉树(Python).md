# LeetCode题解(0968)：计算二叉树中依据指定规则安装监控的最小数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-tree-cameras/)（困难）

标签：树、二叉树、深度优先搜索、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$     | 100ms (5.13%) |
| Ans 2 (Python) | $O(N)$     | $O(H)$     | 52ms (94.87%) |
| Ans 3 (Python) |            |            |               |

解法一（贪心算法）：

```python
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 贪心算法：每个节点在选择装监控的方案时，都尽可能让装的监控更靠近根节点
        # 返回值：1. 当前节点下安装监控的最小数量
        #        2. 当前节点的父节点是否必须安装监控：1=距离最近监控为1个单位距离；2=距离当前最近监控为2个单位距离；3=距离当前最近监控为3个单位距离
        def dfs(node):
            # 处理节点不存在的情况
            if not node:
                return 0, 2

            # 处理节点为叶节点的情况
            if not node.left and not node.right:
                # 处理当前节点为根节点的情况
                if node == root:
                    return 1, 1

                # 处理当前节点不是根节点的情况（与子节点没有安装监控的情况相当）
                else:
                    return 0, 3

            # 处理当前节点不是叶节点的情况
            n_left, d_left = dfs(node.left)
            n_right, d_right = dfs(node.right)
            dd = sorted([d_left, d_right])
            if dd[0] == 1 and dd[1] in {1, 2}:  # 左节点或右节点有一个已经安装监控，且另外一个子结点的至少一个子节点也已经安装监控
                return n_left + n_right, 2
            elif dd[1] == 3:
                return n_left + n_right + 1, 1  # 左节点或右节点中至少有一个的所有子节点都没有安装监控
            else:  # dd = [2,2]  左节点和右节点都没有安装监控，但是它们都至少有一个子节点安装了监控
                if node == root:
                    return n_left + n_right + 1, 1

                # 处理当前节点不是根节点的情况
                else:
                    return n_left + n_right, 3

        return dfs(root)[0]
```

解法二（优化的贪心算法）：

```python
class Solution:
    def __init__(self):
        self.root = None
        self.ans = 0

    def dfs(self, node):
        # 贪心算法：每个节点在选择装监控的方案时，都尽可能让装的监控更靠近根节点
        # 返回值：1. 当前节点下安装监控的最小数量
        #        2. 当前节点的父节点是否必须安装监控：1=距离最近监控为1个单位距离；2=距离当前最近监控为2个单位距离；3=距离当前最近监控为3个单位距离

        # 处理节点不存在的情况
        if not node:
            return 2

        # 处理当前节点不是叶节点的情况
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # dd = [1,3] or [2,3] or [3,3] or [3,2] or [3,1]
        # 情况：左节点或右节点中至少有一个的所有子节点都没有安装监控
        if left == 3 or right == 3:
            self.ans += 1
            return 1

        # dd = [1,1] or [1,2] or [2,1]
        # 情况：左节点或右节点有一个已经安装监控，且另外一个子结点的至少一个子节点也已经安装监控
        elif left == 1 or right == 1:
            return 2

        # dd = [2,2]
        # 情况A：左节点和右节点都没有安装监控，但是它们都至少有一个子节点安装了监控
        # 情况B：当前节点为叶节点
        else:
            if node == self.root:
                self.ans += 1
                return 1
            else:
                return 3

    def minCameraCover(self, root: TreeNode) -> int:
        self.root = root
        self.dfs(root)
        return self.ans
```