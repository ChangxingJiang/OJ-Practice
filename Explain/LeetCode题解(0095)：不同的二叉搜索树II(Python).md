# LeetCode题解(0095)：指定元素能够组成的所有不同的二叉树(Python)

题目：[原题链接](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)（中等）

标签：树、二叉树、递归

| 解法           | 时间复杂度                       | 空间复杂度 | 执行用时      |
| -------------- | -------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×A)$ : 其中A为最终结果的数量 | $O(N×A)$   | 76ms (57.38%) |
| Ans 2 (Python) |                                  |            |               |
| Ans 3 (Python) |                                  |            |               |

解法一：

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def recursor(start, end):
            # 处理没有根节点的情况
            if start > end:
                return [None]

            # 处理只剩一个根节点的情况
            elif start == end:
                return [TreeNode(start)]

            # 处理还有多种根节点的情况
            ans = []
            for i in range(start, end + 1):
                left_trees = recursor(start, i - 1)
                right_trees = recursor(i + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        node = TreeNode(i)
                        node.left = left_tree
                        node.right = right_tree
                        ans.append(node)

            return ans

        return recursor(1, n) if n else []
```