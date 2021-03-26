# LeetCode题解(LCP10)：二叉树任务调度(Python)

题目：[原题链接](https://leetcode-cn.com/problems/er-cha-shu-ren-wu-diao-du/)（困难）

标签：深度优先搜索、动态规划、树、二叉树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 96ms (85.97%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        total_root, full_root = self.dfs(root)
        return total_root - full_root

    def dfs(self, root):
        """深度优先搜索

        :param root: 当前树(子树)的根节点
        :return: 总计运行时间、最大并行时间
        """
        # 处理空节点的情况
        if not root:
            return 0., 0.

        # 递归左子树和右子树
        total_left, full_left = self.dfs(root.left)
        total_right, full_right = self.dfs(root.right)

        # 计算树的总计运行时间
        total_root = root.val + total_left + total_right

        if total_left < total_right:
            total_left, total_right = total_right, total_left
            full_left, full_right = full_right, full_left

        # 处理左子节点和右子节点均可以完全双线程的情况
        if total_left - 2 * full_left <= total_right:
            full_root = (total_left + total_right) / 2

        # 处理左子节点和右子节点不能完全双线程的情况
        else:
            full_root = total_right + full_left

        return total_root, full_root
```



