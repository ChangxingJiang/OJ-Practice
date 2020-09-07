# LeetCode题解(0113)：寻找二叉树中所有根节点到叶节点的路径和为目标值的路径(Python)

题目：[原题链接](https://leetcode-cn.com/problems/path-sum-ii/)（中等）

标签：树、二叉树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度                   | 执行用时      |
| -------------- | ---------- | ---------------------------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(H)$ : 其中H为二叉树的深度 | 52ms (79.88%) |
| Ans 2 (Python) |            |                              |               |
| Ans 3 (Python) |            |                              |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def recursor(node, stack, _sum):
            if node:
                stack.append(node.val)  # 记录当前路径
                _sum += node.val  # 计算当前路径和

                if not node.left and not node.right:
                    if _sum == sum:
                        self.ans.append(stack)
                else:
                    if node.left:
                        recursor(node.left, stack.copy(), _sum)
                    if node.right:
                        recursor(node.right, stack.copy(), _sum)

        recursor(root, [], 0)
        return self.ans
```